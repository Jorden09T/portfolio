package com.example.project2;

import android.os.Bundle;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import android.Manifest;
import android.content.pm.PackageManager;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

public class SMSActivity extends AppCompatActivity {

    private static final int SMS_PERMISSION_CODE = 1;
    private TextView permissionStatus;
    private TextView notificationMessage;
    private Button requestPermissionButton;

    //sms
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sms);

        permissionStatus = findViewById(R.id.permission_status);
        notificationMessage = findViewById(R.id.notification_message);
        requestPermissionButton = findViewById(R.id.request_permission_button);

        checkSmsPermission();

        requestPermissionButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                requestSmsPermission();
            }
        });
    }
    private void checkSmsPermission() {
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.SEND_SMS) == PackageManager.PERMISSION_GRANTED) {
            permissionStatus.setText("Permission Status: Granted");
            notificationMessage.setVisibility(View.VISIBLE);
            notificationMessage.setText("You will receive notifications.");
        } else {
            permissionStatus.setText("Permission Status: Denied");
            notificationMessage.setVisibility(View.GONE);
        }
    }

    private void requestSmsPermission() {
        if (ActivityCompat.shouldShowRequestPermissionRationale(this, Manifest.permission.SEND_SMS)) {
            // Show an explanation to the user why the permission is needed
            // This can be a dialog or a snackbar
        } else {
            ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.SEND_SMS}, SMS_PERMISSION_CODE);
        }
    }


    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode == SMS_PERMISSION_CODE) {
            if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                permissionStatus.setText("Permission Status: Granted");
                notificationMessage.setVisibility(View.VISIBLE);
                notificationMessage.setText("You will receive notifications.");
            } else {
                permissionStatus.setText("Permission Status: Denied");
                notificationMessage.setVisibility(View.GONE);
            }
        }
    }
}