import re

with open("app/src/main/java/com/example/ui/AccountDetailScreen.kt", "r") as f:
    content = f.read()

# Add imports for search and export
imports = """
import androidx.compose.material.icons.filled.Search
import androidx.compose.material.icons.filled.Share
import androidx.compose.material.icons.filled.Close
import android.content.Intent
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.ui.platform.LocalContext
import java.io.OutputStreamWriter
"""
content = content.replace("import androidx.compose.foundation.isSystemInDarkTheme", "import androidx.compose.foundation.isSystemInDarkTheme\n" + imports)

# Add search query state
search_state = """
    var searchQuery by remember { mutableStateOf("") }
    var isSearchActive by remember { mutableStateOf(false) }
    val context = LocalContext.current
"""
content = content.replace("var transactionToDelete by remember { mutableStateOf<Transaction?>(null) }", "var transactionToDelete by remember { mutableStateOf<Transaction?>(null) }\n" + search_state)

# Add CSV Export launcher
export_launcher = """
    val exportLauncher = rememberLauncherForActivityResult(ActivityResultContracts.CreateDocument("text/csv")) { uri ->
        if (uri != null) {
            try {
                context.contentResolver.openOutputStream(uri)?.use { outputStream ->
                    val writer = OutputStreamWriter(outputStream)
                    writer.write("Date,Type,Amount,Note,DueDate\\n")
                    transactions.forEach { tx ->
                        val date = SimpleDateFormat("dd MMM yyyy", Locale.getDefault()).format(Date(tx.timestamp))
                        val type = if (tx.type == TransactionType.GIVEN) "Given" else "Received"
                        val amount = tx.amount
                        val note = tx.note.replace(",", " ")
                        val due = tx.dueDate?.let { SimpleDateFormat("dd MMM yyyy", Locale.getDefault()).format(Date(it)) } ?: ""
                        writer.write("$date,$type,$amount,$note,$due\\n")
                    }
                    writer.flush()
                }
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }
    }
"""
content = content.replace("if (accountWithBalance == null) {", export_launcher + "\n    if (accountWithBalance == null) {")

# Update TopAppBar
top_bar = """
            TopAppBar(
                title = {
                    if (isSearchActive) {
                        OutlinedTextField(
                            value = searchQuery,
                            onValueChange = { searchQuery = it },
                            placeholder = { Text(strings.search + "...") },
                            singleLine = true,
                            modifier = Modifier.fillMaxWidth().padding(end = 8.dp),
                            colors = OutlinedTextFieldDefaults.colors(
                                focusedBorderColor = Color.Transparent,
                                unfocusedBorderColor = Color.Transparent
                            )
                        )
                    } else {
                        Column {
                            Text(accountWithBalance.account.name, fontWeight = FontWeight.Bold, color = textColor)
                            Text(
                                if (accountWithBalance.balance >= 0) "You will get: Rs. ${accountWithBalance.balance.absoluteValue}"
                                else "You will give: Rs. ${accountWithBalance.balance.absoluteValue}",
                                fontSize = 12.sp,
                                color = if (accountWithBalance.balance >= 0) Color(0xFF386a20) else Color(0xFFB3261E)
                            )
                        }
                    }
                },
                navigationIcon = {
                    IconButton(onClick = onNavigateBack) {
                        Icon(Icons.AutoMirrored.Filled.ArrowBack, contentDescription = "Back", tint = textColor)
                    }
                },
                actions = {
                    if (isSearchActive) {
                        IconButton(onClick = { 
                            isSearchActive = false
                            searchQuery = ""
                        }) {
                            Icon(Icons.Default.Close, contentDescription = "Close Search", tint = textColor)
                        }
                    } else {
                        IconButton(onClick = { isSearchActive = true }) {
                            Icon(Icons.Default.Search, contentDescription = "Search", tint = textColor)
                        }
                        IconButton(onClick = { 
                            exportLauncher.launch("${accountWithBalance.account.name}_ledger.csv")
                        }) {
                            Icon(Icons.Default.Share, contentDescription = "Export CSV", tint = textColor)
                        }
                        IconButton(onClick = { menuExpanded = true }) {
                            Icon(Icons.Default.MoreVert, contentDescription = "More", tint = textColor)
                        }
                    }
                    DropdownMenu(
                        expanded = menuExpanded,
                        onDismissRequest = { menuExpanded = false }
                    ) {
                        DropdownMenuItem(
                            text = { Text(strings.editAccountName) },
                            onClick = {
                                menuExpanded = false
                                showEditAccountDialog = true
                            },
                            leadingIcon = { Icon(Icons.Default.Edit, contentDescription = null) }
                        )
                        DropdownMenuItem(
                            text = { Text(strings.deleteAccount) },
                            onClick = {
                                menuExpanded = false
                                showDeleteAccountConfirm = true
                            },
                            leadingIcon = { Icon(Icons.Default.Delete, contentDescription = null, tint = Color(0xFFB3261E)) }
                        )
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(containerColor = surfaceColor)
            )
"""
# Replace old TopAppBar
import re
content = re.sub(r'TopAppBar\(\s*title = \{.*?colors = TopAppBarDefaults\.topAppBarColors\(containerColor = surfaceColor\)\s*\)', top_bar.strip(), content, flags=re.DOTALL)


# Filter transactions
filter_logic = """
                    val filteredTransactions = transactions.filter {
                        val dateStr = SimpleDateFormat("dd MMM yyyy", Locale.getDefault()).format(Date(it.timestamp))
                        it.note.contains(searchQuery, ignoreCase = true) || dateStr.contains(searchQuery, ignoreCase = true)
                    }
                    items(filteredTransactions) { transaction ->
"""
content = content.replace("items(transactions) { transaction ->", filter_logic)

with open("app/src/main/java/com/example/ui/AccountDetailScreen.kt", "w") as f:
    f.write(content)
