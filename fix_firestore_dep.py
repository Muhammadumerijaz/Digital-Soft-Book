import re

with open("app/build.gradle.kts", "r") as f:
    content = f.read()

content = content.replace("implementation(\"com.google.firebase:firebase-firestore-ktx\")", "implementation(\"com.google.firebase:firebase-firestore\")")

with open("app/build.gradle.kts", "w") as f:
    f.write(content)
