import re

with open("app/build.gradle.kts", "r") as f:
    content = f.read()

content = content.replace("  implementation(platform(libs.firebase.bom))", "  implementation(platform(libs.firebase.bom))\n  implementation(\"com.google.firebase:firebase-firestore-ktx\")")

with open("app/build.gradle.kts", "w") as f:
    f.write(content)
