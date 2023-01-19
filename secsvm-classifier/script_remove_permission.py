import os
import subprocess

def remove_suspicious_permission(apk_file):
    # decompile the apk file
    subprocess.call(["apktool", "d", apk_file])
    
    # navigate to the decompiled apk folder
    apk_folder = apk_file.replace(".apk", "")
    os.chdir(apk_folder)
    
    # read the AndroidManifest.xml file
    with open("AndroidManifest.xml", "r") as manifest_file:
        manifest_data = manifest_file.read()
    
    # remove the suspicious permission from the manifest file
    suspicious_permission = "android.permission.READ_PHONE_STATE"
    new_manifest_data = manifest_data.replace(suspicious_permission, "")
    
    # write the new data to the manifest file
    with open("AndroidManifest.xml", "w") as manifest_file:
        manifest_file.write(new_manifest_data)
    
    # recompile the apk
    subprocess.call(["apktool", "b", apk_folder])
    
    # sign the new apk
    new_apk_file = apk_file.replace(".apk", "_fixed.apk")
    subprocess.call(["jarsigner", "-verbose", "-sigalg", "SHA1withRSA", "-digestalg", "SHA1", "-keystore", "mykey.keystore", "-storepass", "mypassword", new_apk_file, "alias_name"])
    
    # remove the decompiled apk folder
    os.chdir("..")
    subprocess.call(["rm", "-r", apk_folder])

# test the function
remove_suspicious_permission("example.apk")
