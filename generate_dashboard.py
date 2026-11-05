import os

dashboard_code = """
package com.example.ui

import android.content.Intent
import android.net.Uri
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Add
import androidx.compose.material.icons.filled.ArrowDownward
import androidx.compose.material.icons.filled.ArrowUpward
import androidx.compose.material.icons.filled.ArrowOutward
import androidx.compose.material.icons.filled.Menu
import androidx.compose.material.icons.filled.Person
import androidx.compose.material.icons.filled.Info
import androidx.compose.material.icons.filled.Language
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.draw.shadow
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import kotlin.math.absoluteValue
import kotlinx.coroutines.launch

@Composable
fun SoftVibeLogo(modifier: Modifier = Modifier, isDark: Boolean = false) {
    val textColor = if (isDark) Color.White else Color(0xFF2C2C34)
    val tealColor = Color(0xFF00C896)
    Row(verticalAlignment = Alignment.CenterVertically, modifier = modifier) {
        Column {
            Row(verticalAlignment = Alignment.Bottom) {
                Text("Soft Vibe", fontSize = 24.sp, fontWeight = FontWeight.Bold, color = textColor)
                Icon(Icons.Default.ArrowOutward, contentDescription = null, tint = tealColor, modifier = Modifier.size(28.dp).padding(bottom = 4.dp))
            }
            Text("Tech Solutions", fontSize = 12.sp, fontWeight = FontWeight.Medium, color = textColor.copy(alpha = 0.7f), modifier = Modifier.padding(start = 2.dp))
        }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun DashboardScreen(
    viewModel: KhataViewModel,
    onNavigateToAccount: (Int) -> Unit
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()
    val strings = getStrings(uiState.currentLanguage)
    var showAddAccountDialog by remember { mutableStateOf(false) }
    var showAddProfileDialog by remember { mutableStateOf(false) }
    var showEditProfileDialog by remember { mutableStateOf(false) }
    var showDeleteProfileConfirm by remember { mutableStateOf(false) }

    val drawerState = rememberDrawerState(initialValue = DrawerValue.Closed)
    val scope = rememberCoroutineScope()
    val context = LocalContext.current
    val isDark = isSystemInDarkTheme()
    
    val currentProfile = uiState.profiles.find { it.id == uiState.currentProfileId }
    
    val bgColor = if (isDark) Color(0xFF121212) else Color(0xFFF7F2FA)
    val surfaceColor = if (isDark) Color(0xFF1E1E1E) else Color.White
    val textColor = if (isDark) Color.White else Color(0xFF1D1B20)
    val textSecColor = if (isDark) Color.LightGray else Color(0xFF49454F)

    ModalNavigationDrawer(
        drawerState = drawerState,
        drawerContent = {
            ModalDrawerSheet(drawerContainerColor = surfaceColor) {
                Spacer(Modifier.height(24.dp))
                SoftVibeLogo(modifier = Modifier.padding(16.dp), isDark = isDark)
                Spacer(Modifier.height(16.dp))
                Divider()
                Spacer(Modifier.height(16.dp))
                
                Text(
                    "Language",
                    fontSize = 14.sp,
                    fontWeight = FontWeight.Bold,
                    color = textSecColor,
                    modifier = Modifier.padding(horizontal = 24.dp, vertical = 8.dp)
                )
                val langs = listOf(AppLanguage.ENGLISH to "English", AppLanguage.URDU to "اردو (Urdu)", AppLanguage.ROMAN_URDU to "Roman Urdu")
                langs.forEach { (lang, label) ->
                    NavigationDrawerItem(
                        label = { Text(label, color = textColor) },
                        selected = uiState.currentLanguage == lang,
                        onClick = { 
                            viewModel.setLanguage(lang)
                            scope.launch { drawerState.close() }
                        },
                        icon = { Icon(Icons.Default.Language, contentDescription = null, tint = textColor) },
                        modifier = Modifier.padding(horizontal = 12.dp)
                    )
                }
                
                Spacer(Modifier.height(16.dp))
                Divider()
                Spacer(Modifier.height(16.dp))
                
                Text(
                    "About",
                    fontSize = 14.sp,
                    fontWeight = FontWeight.Bold,
                    color = textSecColor,
                    modifier = Modifier.padding(horizontal = 24.dp, vertical = 8.dp)
                )
                NavigationDrawerItem(
                    label = { Text("App Info", color = textColor) },
                    selected = false,
                    onClick = { },
                    icon = { Icon(Icons.Default.Info, contentDescription = null, tint = textColor) },
                    modifier = Modifier.padding(horizontal = 12.dp)
                )
                Spacer(Modifier.height(8.dp))
                Text(
                    text = "Developed by Soft Vibe Tech",
                    fontSize = 12.sp,
                    color = textSecColor,
                    modifier = Modifier.padding(horizontal = 24.dp)
                )
                Spacer(Modifier.height(16.dp))
                Row(modifier = Modifier.padding(horizontal = 24.dp), horizontalArrangement = Arrangement.spacedBy(16.dp)) {
                    Button(onClick = {
                        context.startActivity(Intent(Intent.ACTION_VIEW, Uri.parse("https://www.facebook.com/SoftVibeTech")))
                    }) {
                        Text("Facebook")
                    }
                }
                Spacer(Modifier.height(8.dp))
                Row(modifier = Modifier.padding(horizontal = 24.dp)) {
                    Button(onClick = {
                        context.startActivity(Intent(Intent.ACTION_VIEW, Uri.parse("https://linkedin.com/company/softvibetech")))
                    }) {
                        Text("LinkedIn")
                    }
                }
            }
        }
    ) {
        Scaffold(
            containerColor = bgColor,
            floatingActionButton = {
                FloatingActionButton(
                    onClick = { showAddAccountDialog = true },
                    containerColor = Color(0xFFD0BCFF),
                    contentColor = Color(0xFF381E72),
                    shape = RoundedCornerShape(16.dp),
                    elevation = FloatingActionButtonDefaults.elevation(defaultElevation = 6.dp)
                ) {
                    Icon(Icons.Default.Add, contentDescription = "Add Account", modifier = Modifier.size(28.dp))
                }
            },
            floatingActionButtonPosition = FabPosition.Center
        ) { padding ->
            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(padding)
            ) {
                // Header
                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(horizontal = 20.dp, vertical = 24.dp),
                    horizontalArrangement = Arrangement.SpaceBetween,
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        IconButton(onClick = { scope.launch { drawerState.open() } }) {
                            Icon(Icons.Default.Menu, contentDescription = "Menu", tint = textColor)
                        }
                        Spacer(modifier = Modifier.width(8.dp))
                        Column {
                            Text(
                                text = "DIGITAL SOFT BOOK",
                                fontSize = 12.sp,
                                fontWeight = FontWeight.Medium,
                                color = textSecColor,
                                letterSpacing = 1.sp
                            )
                            Text(
                                text = currentProfile?.name ?: "Dashboard",
                                fontSize = 24.sp,
                                fontWeight = FontWeight.SemiBold,
                                color = textColor
                            )
                        }
                    }
                    
                    Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                        var profileMenu by remember { mutableStateOf(false) }
                        Box {
                            Box(
                                modifier = Modifier
                                    .size(40.dp)
                                    .background(Color(0xFFD0BCFF), CircleShape)
                                    .shadow(1.dp, CircleShape)
                                    .clickable { profileMenu = true },
                                contentAlignment = Alignment.Center
                            ) {
                                Icon(Icons.Default.Person, contentDescription = "Profile", tint = Color(0xFF381E72))
                            }
                            DropdownMenu(expanded = profileMenu, onDismissRequest = { profileMenu = false }) {
                                uiState.profiles.forEach { profile ->
                                    DropdownMenuItem(
                                        text = { Text(profile.name, fontWeight = if (uiState.currentProfileId == profile.id) FontWeight.Bold else FontWeight.Normal) },
                                        onClick = { 
                                            viewModel.setProfile(profile.id)
                                            profileMenu = false
                                        }
                                    )
                                }
                                Divider()
                                DropdownMenuItem(
                                    text = { Text("Edit Profile") },
                                    onClick = {
                                        profileMenu = false
                                        showEditProfileDialog = true
                                    }
                                )
                                if (currentProfile?.id != 1) {
                                    DropdownMenuItem(
                                        text = { Text("Delete Profile") },
                                        onClick = {
                                            profileMenu = false
                                            showDeleteProfileConfirm = true
                                        }
                                    )
                                }
                                Divider()
                                DropdownMenuItem(
                                    text = { Text("Add Profile") },
                                    onClick = {
                                        profileMenu = false
                                        showAddProfileDialog = true
                                    }
                                )
                            }
                        }
                    }
                }

                // Balance Card
                Card(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(horizontal = 20.dp),
                    shape = RoundedCornerShape(24.dp),
                    colors = CardDefaults.cardColors(containerColor = surfaceColor),
                    elevation = CardDefaults.cardElevation(defaultElevation = 0.dp)
                ) {
                    Column(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(24.dp)
                    ) {
                        Text(
                            text = strings.netBalance,
                            fontSize = 14.sp,
                            color = textSecColor
                        )
                        val balColor = if (uiState.overallBalance >= 0) Color(0xFF386a20) else Color(0xFFB3261E)
                        Text(
                            text = "Rs. ${"%.0f".format(uiState.overallBalance.absoluteValue)}",
                            fontSize = 36.sp,
                            fontWeight = FontWeight.Bold,
                            color = if (isDark) textColor else balColor,
                            modifier = Modifier.padding(vertical = 4.dp)
                        )
                        
                        Spacer(modifier = Modifier.height(16.dp))
                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.spacedBy(16.dp)
                        ) {
                            Card(
                                modifier = Modifier
                                    .weight(1f)
                                    .height(112.dp),
                                shape = RoundedCornerShape(24.dp),
                                colors = CardDefaults.cardColors(containerColor = if (isDark) Color(0xFF3A2321) else Color(0xFFFFDAD6)),
                                elevation = CardDefaults.cardElevation(defaultElevation = 0.dp)
                            ) {
                                Column(
                                    modifier = Modifier
                                        .fillMaxSize()
                                        .padding(16.dp),
                                    verticalArrangement = Arrangement.SpaceBetween
                                ) {
                                    Box(
                                        modifier = Modifier
                                            .size(32.dp)
                                            .background(Color.White.copy(alpha = 0.4f), CircleShape),
                                        contentAlignment = Alignment.Center
                                    ) {
                                        Icon(
                                            Icons.Default.ArrowDownward,
                                            contentDescription = null,
                                            modifier = Modifier.size(16.dp),
                                            tint = if (isDark) Color(0xFFFFB4AB) else Color(0xFF601410)
                                        )
                                    }
                                    Column {
                                        Text(
                                            text = strings.given.uppercase(),
                                            fontSize = 10.sp,
                                            fontWeight = FontWeight.Bold,
                                            color = if (isDark) Color(0xFFFFB4AB).copy(alpha=0.8f) else Color(0xFF601410).copy(alpha = 0.7f)
                                        )
                                        Text(
                                            text = "Rs. ${"%.0f".format(uiState.totalReceived)}",
                                            fontSize = 20.sp,
                                            fontWeight = FontWeight.Bold,
                                            color = if (isDark) Color.White else Color(0xFF601410)
                                        )
                                    }
                                }
                            }
                            Card(
                                modifier = Modifier
                                    .weight(1f)
                                    .height(112.dp),
                                shape = RoundedCornerShape(24.dp),
                                colors = CardDefaults.cardColors(containerColor = if (isDark) Color(0xFF003355) else Color(0xFFC2E7FF)),
                                elevation = CardDefaults.cardElevation(defaultElevation = 0.dp)
                            ) {
                                Column(
                                    modifier = Modifier
                                        .fillMaxSize()
                                        .padding(16.dp),
                                    verticalArrangement = Arrangement.SpaceBetween
                                ) {
                                    Box(
                                        modifier = Modifier
                                            .size(32.dp)
                                            .background(Color.White.copy(alpha = 0.4f), CircleShape),
                                        contentAlignment = Alignment.Center
                                    ) {
                                        Icon(
                                            Icons.Default.ArrowUpward,
                                            contentDescription = null,
                                            modifier = Modifier.size(16.dp),
                                            tint = if (isDark) Color(0xFF76C4FF) else Color(0xFF001D35)
                                        )
                                    }
                                    Column {
                                        Text(
                                            text = strings.received.uppercase(),
                                            fontSize = 10.sp,
                                            fontWeight = FontWeight.Bold,
                                            color = if (isDark) Color(0xFF76C4FF).copy(alpha=0.8f) else Color(0xFF001D35).copy(alpha = 0.7f)
                                        )
                                        Text(
                                            text = "Rs. ${"%.0f".format(uiState.totalGiven)}",
                                            fontSize = 20.sp,
                                            fontWeight = FontWeight.Bold,
                                            color = if (isDark) Color.White else Color(0xFF001D35)
                                        )
                                    }
                                }
                            }
                        }
                    }
                }

                Spacer(modifier = Modifier.height(24.dp))

                Box(
                    modifier = Modifier
                        .fillMaxSize()
                        .clip(RoundedCornerShape(topStart = 32.dp, topEnd = 32.dp))
                        .background(surfaceColor)
                ) {
                    Column(
                        modifier = Modifier
                            .fillMaxSize()
                            .padding(20.dp)
                    ) {
                        Text(
                            text = strings.accountsList,
                            fontSize = 18.sp,
                            fontWeight = FontWeight.SemiBold,
                            color = textColor
                        )
                        Spacer(modifier = Modifier.height(16.dp))
                        LazyColumn(
                            modifier = Modifier.fillMaxSize(),
                            verticalArrangement = Arrangement.spacedBy(12.dp)
                        ) {
                            items(uiState.accounts) { accountWithBalance ->
                                AccountItem(
                                    accountWithBalance = accountWithBalance,
                                    strings = strings,
                                    isDark = isDark,
                                    onClick = { onNavigateToAccount(accountWithBalance.account.id) }
                                )
                            }
                            item { Spacer(modifier = Modifier.height(100.dp)) }
                        }
                    }
                }
            }
        }
    }

    if (showAddAccountDialog) {
        var accountName by remember { mutableStateOf("") }
        AlertDialog(
            onDismissRequest = { showAddAccountDialog = false },
            title = { Text(strings.addAccount) },
            text = {
                OutlinedTextField(
                    value = accountName,
                    onValueChange = { accountName = it },
                    label = { Text(strings.accountNameHint) },
                    singleLine = true
                )
            },
            confirmButton = {
                Button(onClick = {
                    viewModel.addAccount(accountName)
                    showAddAccountDialog = false
                }) {
                    Text(strings.add)
                }
            },
            dismissButton = {
                TextButton(onClick = { showAddAccountDialog = false }) {
                    Text(strings.cancel)
                }
            }
        )
    }

    if (showAddProfileDialog) {
        var profileName by remember { mutableStateOf("") }
        AlertDialog(
            onDismissRequest = { showAddProfileDialog = false },
            title = { Text("Add Profile") },
            text = {
                OutlinedTextField(
                    value = profileName,
                    onValueChange = { profileName = it },
                    label = { Text("Profile Name") },
                    singleLine = true
                )
            },
            confirmButton = {
                Button(onClick = {
                    viewModel.addProfile(profileName)
                    showAddProfileDialog = false
                }) {
                    Text("Add")
                }
            },
            dismissButton = {
                TextButton(onClick = { showAddProfileDialog = false }) {
                    Text("Cancel")
                }
            }
        )
    }

    if (showEditProfileDialog && currentProfile != null) {
        var profileName by remember { mutableStateOf(currentProfile.name) }
        AlertDialog(
            onDismissRequest = { showEditProfileDialog = false },
            title = { Text("Edit Profile") },
            text = {
                OutlinedTextField(
                    value = profileName,
                    onValueChange = { profileName = it },
                    label = { Text("Profile Name") },
                    singleLine = true
                )
            },
            confirmButton = {
                Button(onClick = {
                    viewModel.updateProfileName(currentProfile, profileName)
                    showEditProfileDialog = false
                }) {
                    Text("Save")
                }
            },
            dismissButton = {
                TextButton(onClick = { showEditProfileDialog = false }) {
                    Text("Cancel")
                }
            }
        )
    }

    if (showDeleteProfileConfirm && currentProfile != null) {
        AlertDialog(
            onDismissRequest = { showDeleteProfileConfirm = false },
            title = { Text("Delete Profile") },
            text = { Text("Are you sure you want to delete this profile? All accounts inside will become inaccessible.") },
            confirmButton = {
                Button(
                    onClick = {
                        viewModel.deleteProfile(currentProfile)
                        showDeleteProfileConfirm = false
                    },
                    colors = ButtonDefaults.buttonColors(containerColor = Color(0xFFB3261E))
                ) {
                    Text("Delete")
                }
            },
            dismissButton = {
                TextButton(onClick = { showDeleteProfileConfirm = false }) {
                    Text("Cancel")
                }
            }
        )
    }
}

@Composable
fun AccountItem(accountWithBalance: AccountWithBalance, strings: AppStrings, isDark: Boolean, onClick: () -> Unit) {
    val colors = listOf(Color(0xFF6750A4), Color(0xFF006391), Color(0xFF516300), Color(0xFF8C1D18))
    val avatarColor = colors[accountWithBalance.account.name.length % colors.size]
    
    val initial = accountWithBalance.account.name.firstOrNull()?.uppercase() ?: "?"
    val textColor = if (isDark) Color.White else Color(0xFF1D1B20)
    val textSecColor = if (isDark) Color.LightGray else Color(0xFF49454F)
    val bgColor = if (isDark) Color(0xFF2C2C2C) else Color(0xFFF7F2FA)

    Row(
        modifier = Modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(16.dp))
            .background(bgColor)
            .clickable { onClick() }
            .padding(12.dp),
        horizontalArrangement = Arrangement.SpaceBetween,
        verticalAlignment = Alignment.CenterVertically
    ) {
        Row(
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.spacedBy(12.dp)
        ) {
            Box(
                modifier = Modifier
                    .size(48.dp)
                    .clip(CircleShape)
                    .background(avatarColor),
                contentAlignment = Alignment.Center
            ) {
                Text(
                    text = initial,
                    color = Color.White,
                    fontSize = 20.sp,
                    fontWeight = FontWeight.Medium
                )
            }
            Column {
                Text(
                    text = accountWithBalance.account.name,
                    fontSize = 14.sp,
                    fontWeight = FontWeight.Bold,
                    color = textColor
                )
                Text(
                    text = if (accountWithBalance.balance == 0.0) strings.noBalance else strings.activeAccount,
                    fontSize = 12.sp,
                    color = textSecColor
                )
            }
        }
        
        Column(horizontalAlignment = Alignment.End) {
            val balColor = if (isDark) {
                if (accountWithBalance.balance >= 0) Color(0xFF90EE90) else Color(0xFFFFB4AB)
            } else {
                if (accountWithBalance.balance >= 0) Color(0xFF386a20) else Color(0xFFB3261E)
            }
            val sign = if (accountWithBalance.balance >= 0) "+" else "-"
            Text(
                text = "${sign} Rs. ${"%.0f".format(accountWithBalance.balance.absoluteValue)}",
                fontSize = 14.sp,
                fontWeight = FontWeight.Bold,
                color = balColor
            )
            Text(
                text = if (accountWithBalance.balance >= 0) strings.youAreOwed else strings.youOwe,
                fontSize = 10.sp,
                color = textSecColor
            )
        }
    }
}
"""

with open("app/src/main/java/com/example/ui/DashboardScreen.kt", "w") as f:
    f.write(dashboard_code)
