import re

with open("app/src/main/java/com/example/ui/DashboardScreen.kt", "r") as f:
    content = f.read()

content = content.replace("import androidx.compose.material.icons.filled.Info", "import androidx.compose.material.icons.filled.Info\nimport androidx.compose.material.icons.filled.CloudUpload\nimport android.widget.Toast")

drawer_mod = """
                Spacer(Modifier.height(16.dp))
                Divider()
                Spacer(Modifier.height(16.dp))
                
                Text(
                    "Cloud Sync",
                    fontSize = 14.sp,
                    fontWeight = FontWeight.Bold,
                    color = textSecColor,
                    modifier = Modifier.padding(horizontal = 24.dp, vertical = 8.dp)
                )
                NavigationDrawerItem(
                    label = { Text("Backup to Firestore", color = textColor) },
                    selected = false,
                    onClick = { 
                        scope.launch { drawerState.close() }
                        if (currentProfile != null) {
                            Toast.makeText(context, "Starting backup...", Toast.LENGTH_SHORT).show()
                            viewModel.backupToCloud(currentProfile.id, currentProfile.name) { success ->
                                val msg = if (success) "Backup successful!" else "Backup failed. Check if Firebase is configured via google-services.json"
                                Toast.makeText(context, msg, Toast.LENGTH_LONG).show()
                            }
                        }
                    },
                    icon = { Icon(Icons.Default.CloudUpload, contentDescription = null, tint = textColor) },
                    modifier = Modifier.padding(horizontal = 12.dp)
                )
                
                Spacer(Modifier.height(16.dp))
                Divider()
                Spacer(Modifier.height(16.dp))
                
                Text(
                    "About",
"""

content = content.replace("""
                Spacer(Modifier.height(16.dp))
                Divider()
                Spacer(Modifier.height(16.dp))
                
                Text(
                    "About",
""", drawer_mod)

with open("app/src/main/java/com/example/ui/DashboardScreen.kt", "w") as f:
    f.write(content)
