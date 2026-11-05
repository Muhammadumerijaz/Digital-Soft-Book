# 📘 Digital Soft Book


<img width="250" height="500" alt="0" src="https://github.com/user-attachments/assets/40d39876-5ed1-4a27-8c64-a5f5e3e99440" />
<img width="250" height="500" alt="1" src="https://github.com/user-attachments/assets/cc2bc048-9e78-4e99-9ee1-cf4c853974fc" />
<img width="250" height="500" alt="5" src="https://github.com/user-attachments/assets/6fed027e-0375-41cb-a049-65dcb5152910" />
<img width="250" height="500" alt="4" src="https://github.com/user-attachments/assets/e5737136-e948-4e9e-a0f6-46c70eca83e6" />
<img width="250" height="500" alt="3" src="https://github.com/user-attachments/assets/b313ec4b-67eb-4fa1-b5e4-05f79e0b3ab3" />
<img width="250" height="500" alt="6" src="https://github.com/user-attachments/assets/3d3e3ef9-22fc-47a0-90ca-a0b5882c0909" />





### A simple, profile-based digital khata for tracking money given and received.

**Keep every account organised. Understand balances at a glance.**

[![Android](https://img.shields.io/badge/Platform-Android-3DDC84?logo=android&logoColor=white)](https://developer.android.com/)
[![Kotlin](https://img.shields.io/badge/Language-Kotlin-7F52FF?logo=kotlin&logoColor=white)](https://kotlinlang.org/)
[![Jetpack
Compose](https://img.shields.io/badge/UI-Jetpack%20Compose-4285F4?logo=jetpackcompose&logoColor=white)](https://developer.android.com/compose)
[![License](https://img.shields.io/badge/License-See%20repository-lightgrey)](LICENSE)

[Get the Download APP](https://github.com/Muhammadumerijaz/Digital-Soft-Book/blob/main/Digital%20Soft%20Book_1.0%20(1)%20(1).apk) 
[Source code](https://github.com/Muhammadumerijaz/Digital-Soft-Book) ·
[Project page](https://softvibetech.itch.io/digital-soft-book)
[Get the APK](https://github.com/Muhammadumerijaz/Digital-Soft-Book)
:::

------------------------------------------------------------------------

## ✨ About the project

**Digital Soft Book** is an Android khata / personal ledger application
designed to help organise money given to and received from different
people or accounts. Its dashboard presents an overall balance, totals,
and a list of account balances so that the user can quickly understand
their records.

The repository identifies the project as **Digital Soft Book 1.0**. The
interface code in the repository includes profile management, account
creation, language selection, and light/dark theme-aware layouts.

## 🌟 Features

-   **At-a-glance dashboard** --- view the overall balance and the
    totals shown for money given and received.
-   **Separate accounts** --- create named accounts and review each
    account's balance.
-   **Multiple profiles** --- add, switch, edit, and delete profiles.
-   **Three interface languages** --- English, Urdu, and Roman Urdu
    options are present in the dashboard.
-   **Theme-aware interface** --- dashboard components adapt to light
    and dark system themes.
-   **Account status indicators** --- see whether an account has a
    balance and whether the balance indicates money owed to you or money
    you owe.
-   **Android-native UI** --- built with Kotlin and Jetpack Compose /
    Material 3 components.
-   **Backend / AI configuration points** --- the repository includes
    Firebase-related build configuration scripts and a Gemini API
    environment example. Configure credentials securely and verify the
    relevant service implementation before enabling integrations.

> Feature descriptions are based on the files currently visible in this
> repository. Exact transaction workflows, synchronisation behaviour,
> and AI features should be confirmed against the complete app source
> and a running build before being documented as guaranteed
> capabilities.

## 📱 Download

The repository currently lists an Android APK:

-   Open the [GitHub
    repository](https://github.com/Muhammadumerijaz/Digital-Soft-Book).
-   Select `Digital Soft Book_1.0 (1) (1).apk`.
-   Open the file and use GitHub's **Download raw file** option.

Only install APKs from a source you trust. Android may ask you to allow
installation from your browser or file manager.

The itch.io project page is also listed here: [Digital Soft Book on
itch.io](https://softvibetech.itch.io/digital-soft-book). If that page
is unavailable, use the GitHub repository as the current download
location.

## 🧰 Tech stack & project files

  -----------------------------------------------------------------------
  Area                                Repository evidence
  ----------------------------------- -----------------------------------
  Platform                            Android

  Main language / UI                  Kotlin, Jetpack Compose

  UI components                       Material 3

  Build system                        Gradle Kotlin DSL

  Firebase                            Firebase-related Gradle
                                      configuration and Firestore
                                      dependency helper

  AI configuration                    `.env.example` references
                                      `GEMINI_API_KEY`
  -----------------------------------------------------------------------

Useful repository files include:

-   `build.gradle.kts`, `settings.gradle.kts`, `gradle.properties` ---
    Gradle project configuration.
-   `.env.example` --- example Gemini API key variable.
-   `generate_dashboard.py` --- contains generated Kotlin dashboard UI
    code.
-   `update_firebase.py` --- helper script that modifies the app Gradle
    file to add Firestore.
-   `Digital Soft Book.7z`, `khata_project.zip` --- project archives
    listed in the repository.
-   `Digital Soft Book_1.0 (1) (1).apk` --- Android package listed in
    the repository.

## 🚀 Run locally

### Requirements

-   Android Studio (current stable version recommended)
-   Android SDK compatible with the project configuration
-   JDK version required by the Gradle / Android Gradle Plugin
    configuration
-   A physical Android device or emulator

### Steps

1.  Clone or download the repository:

    ``` bash
    git clone https://github.com/Muhammadumerijaz/Digital-Soft-Book.git
    cd Digital-Soft-Book
    ```

2.  Open the project directory in Android Studio.

3.  Allow Android Studio to sync Gradle and resolve any required SDK
    components.

4.  Review `.env.example` and the app's secrets configuration. If the
    build requires a Gemini key, create the required local secrets
    file/configuration and provide your own key.

5.  Never commit real API keys, service-account files, signing
    credentials, or other secrets.

6.  Review `app/build.gradle.kts` and the signing configuration before
    building. The repository's original setup notes mention removing a
    debug signing configuration line if it prevents local execution;
    inspect the current file before changing it.

7.  Select an emulator or connected device and run the app.

> The exact module path, SDK/JDK versions, and secrets plugin setup
> should be confirmed in Android Studio from the complete project
> archive. Do not copy a real API key into a public repository.

## 🔐 Security notes

-   Keep `GEMINI_API_KEY` private. Use local environment/secrets
    configuration for development.
-   Do not publish Firebase service-account credentials or private
    signing keys.
-   If a key was ever committed publicly, revoke or rotate it.
-   Review Firebase security rules before using real financial or
    personal records.
-   Treat the APK as unverified until you have checked its origin,
    signature, and integrity.

## 🗺️ Roadmap

Possible areas for future improvement (not claims about existing
functionality):

-   Add export and restore options for khata records.
-   Add search, filters, and date-based summaries.
-   Add clear transaction history and printable reports.
-   Add automated tests for balance calculations.
-   Document backup, privacy, and data-sync behaviour.
-   Publish versioned releases with checksums and release notes.

## 🤝 Contributing

Contributions, bug reports, and suggestions are welcome.

1.  Fork the repository.
2.  Create a focused branch.
3.  Make and test your changes.
4.  Open a pull request with a clear summary and screenshots where
    useful.

Please avoid including personal financial data, API keys, or credentials
in issues and pull requests.

## 👨‍💻 Credits

**Created by Muhammad Umer Ijaz**\
Project / brand: **Soft Vibe Tech**

-   GitHub: [@Muhammadumerijaz](https://github.com/Muhammadumerijaz)
-   LinkedIn: [Muhammad Umer
    Ijaz](https://www.linkedin.com/in/muhammadumerijaz/)
-   Soft Vibe Tech: [itch.io project
    page](https://softvibetech.itch.io/digital-soft-book)

## 📄 License

No license file was visible in the repository when this README was
prepared. Until a `LICENSE` file is added, reuse, redistribution, and
modification permissions are not explicitly granted. Add the license
that matches the author's intent.

------------------------------------------------------------------------


**Digital Soft Book ---**

Copyright **Soft Vibe Tech**.
:::
