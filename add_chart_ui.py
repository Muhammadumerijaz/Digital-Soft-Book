import re

with open("app/src/main/java/com/example/ui/DashboardScreen.kt", "r") as f:
    content = f.read()

chart_code = """
@Composable
fun SimpleBarChart(given: Double, received: Double, isDark: Boolean) {
    val maxVal = maxOf(given, received, 1.0)
    val givenRatio = (given / maxVal).toFloat()
    val receivedRatio = (received / maxVal).toFloat()
    
    val givenColor = if (isDark) Color(0xFFFFB4AB) else Color(0xFFB3261E)
    val receivedColor = if (isDark) Color(0xFF90EE90) else Color(0xFF386a20)
    
    Column(modifier = Modifier.fillMaxWidth().padding(horizontal = 20.dp)) {
        Text("Last 30 Days Summary", fontSize = 16.sp, fontWeight = FontWeight.Bold, color = if (isDark) Color.White else Color(0xFF1D1B20), modifier = Modifier.padding(bottom = 12.dp))
        Row(modifier = Modifier.fillMaxWidth().height(120.dp), horizontalArrangement = Arrangement.SpaceEvenly, verticalAlignment = Alignment.Bottom) {
            // Given Bar
            Column(horizontalAlignment = Alignment.CenterHorizontally, modifier = Modifier.weight(1f)) {
                Text("Rs. ${"%.0f".format(given)}", fontSize = 12.sp, color = givenColor, fontWeight = FontWeight.Bold)
                Spacer(modifier = Modifier.height(4.dp))
                Box(
                    modifier = Modifier
                        .fillMaxWidth(0.5f)
                        .fillMaxHeight(givenRatio)
                        .clip(RoundedCornerShape(topStart = 8.dp, topEnd = 8.dp))
                        .background(givenColor)
                )
                Spacer(modifier = Modifier.height(8.dp))
                Text("Given", fontSize = 12.sp, color = if (isDark) Color.LightGray else Color.Gray)
            }
            
            // Received Bar
            Column(horizontalAlignment = Alignment.CenterHorizontally, modifier = Modifier.weight(1f)) {
                Text("Rs. ${"%.0f".format(received)}", fontSize = 12.sp, color = receivedColor, fontWeight = FontWeight.Bold)
                Spacer(modifier = Modifier.height(4.dp))
                Box(
                    modifier = Modifier
                        .fillMaxWidth(0.5f)
                        .fillMaxHeight(receivedRatio)
                        .clip(RoundedCornerShape(topStart = 8.dp, topEnd = 8.dp))
                        .background(receivedColor)
                )
                Spacer(modifier = Modifier.height(8.dp))
                Text("Received", fontSize = 12.sp, color = if (isDark) Color.LightGray else Color.Gray)
            }
        }
    }
}
"""

content = content.replace("import androidx.compose.ui.unit.sp", "import androidx.compose.ui.unit.sp\nimport androidx.compose.foundation.layout.fillMaxHeight")

# Inject SimpleBarChart Composable
content = content + "\n" + chart_code

# Add it after Balance Card
insertion_point = "Spacer(modifier = Modifier.height(24.dp))"
replacement = "Spacer(modifier = Modifier.height(24.dp))\n                SimpleBarChart(given = uiState.last30DaysGiven, received = uiState.last30DaysReceived, isDark = isDark)\n                Spacer(modifier = Modifier.height(24.dp))"

content = content.replace(insertion_point, replacement, 1) # Only first occurrence

with open("app/src/main/java/com/example/ui/DashboardScreen.kt", "w") as f:
    f.write(content)

