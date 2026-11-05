import re

with open("app/src/main/java/com/example/ui/KhataViewModel.kt", "r") as f:
    content = f.read()

content = content.replace("import kotlinx.coroutines.flow.flatMapLatest", "import kotlinx.coroutines.flow.flatMapLatest\nimport com.example.data.FirestoreSyncService\nimport kotlinx.coroutines.flow.first")

sync_func = """
    private val firestoreSync = FirestoreSyncService()
    
    fun backupToCloud(profileId: Int, profileName: String, onResult: (Boolean) -> Unit) {
        viewModelScope.launch {
            try {
                val accounts = repository.getAllAccounts(profileId).first()
                val transactions = repository.allTransactions.first().filter { tx -> 
                    accounts.any { it.id == tx.accountId }
                }
                
                val success = firestoreSync.backupProfileData(profileId, profileName, accounts, transactions)
                onResult(success)
            } catch (e: Exception) {
                onResult(false)
            }
        }
    }
"""
content = content.replace("fun deleteProfile(profile: Profile)", sync_func + "\n    fun deleteProfile(profile: Profile)")

with open("app/src/main/java/com/example/ui/KhataViewModel.kt", "w") as f:
    f.write(content)

