import re

with open("app/src/main/java/com/example/ui/KhataViewModel.kt", "r") as f:
    content = f.read()

# Add last 30 days data to DashboardUiState
ui_state_mod = """
    val currentProfileId: Int = 1,
    val last30DaysGiven: Double = 0.0,
    val last30DaysReceived: Double = 0.0
"""
content = content.replace("val currentProfileId: Int = 1\n)", ui_state_mod + "\n)")

# Calculate 30 days data in combine
calc_mod = """
        var totalGiven = 0.0
        var totalReceived = 0.0
        var last30DaysGiven = 0.0
        var last30DaysReceived = 0.0
        
        val thirtyDaysAgo = System.currentTimeMillis() - (30L * 24 * 60 * 60 * 1000)
"""
content = content.replace("var totalGiven = 0.0\n        var totalReceived = 0.0", calc_mod)

acc_mod = """
            val given = accTxs.filter { it.type == TransactionType.GIVEN }.sumOf { it.amount }
            val received = accTxs.filter { it.type == TransactionType.RECEIVED }.sumOf { it.amount }
            
            val recentGiven = accTxs.filter { it.type == TransactionType.GIVEN && it.timestamp >= thirtyDaysAgo }.sumOf { it.amount }
            val recentReceived = accTxs.filter { it.type == TransactionType.RECEIVED && it.timestamp >= thirtyDaysAgo }.sumOf { it.amount }
            
            totalGiven += given
            totalReceived += received
            last30DaysGiven += recentGiven
            last30DaysReceived += recentReceived
"""
content = content.replace("""val given = accTxs.filter { it.type == TransactionType.GIVEN }.sumOf { it.amount }
            val received = accTxs.filter { it.type == TransactionType.RECEIVED }.sumOf { it.amount }
            
            totalGiven += given
            totalReceived += received""", acc_mod)

dashboard_mod = """
            overallBalance = totalGiven - totalReceived,
            currentLanguage = language,
            currentProfileId = currentProfileId,
            last30DaysGiven = last30DaysGiven,
            last30DaysReceived = last30DaysReceived
"""
content = content.replace("""overallBalance = totalGiven - totalReceived,
            currentLanguage = language,
            currentProfileId = currentProfileId""", dashboard_mod)

with open("app/src/main/java/com/example/ui/KhataViewModel.kt", "w") as f:
    f.write(content)

