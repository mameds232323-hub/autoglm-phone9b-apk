[app]
title = AutoGLM Phone 9B APK
package.name = autoglmphone9b
package.domain = com.autoglm.phone9b
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,yaml
version = 9.0
requirements = python3,kivy,pyjnius,android,requests,pillow
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,ACCESS_NETWORK_STATE,QUERY_ALL_PACKAGES,SYSTEM_ALERT_WINDOW,FOREGROUND_SERVICE
android.archs = arm64-v8a, armeabi-v7a
android.api = 33
android.minapi = 26
android.accept_sdk_license_agreements = True

[buildozer]
log_level = 2
warn_on_root = 1
