package com.example.project2;

import android.content.Intent;
import android.os.Bundle;

import android.widget.Button;
import android.widget.EditText;
import android.content.ContentValues;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private EditText editUsername, editPassword;
    private Button buttonSubmit, buttonRegister;
    private SQLiteDatabase db;

    //sms
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        editUsername = findViewById(R.id.editUsername);
        editPassword = findViewById(R.id.editPassword);
        buttonSubmit = findViewById(R.id.buttonSubmit);
        buttonRegister = findViewById(R.id.buttonRegister);

        //initialize Database
        DatabaseHelper dbHelper = new DatabaseHelper(this);
        db = dbHelper.getWritableDatabase();

        buttonSubmit.setOnClickListener(view -> loginUser());
        buttonRegister.setOnClickListener(view -> registerUser());
    }

    private void loginUser(){
        String username = editUsername.getText().toString();
        String password = editPassword.getText().toString();

        Cursor cursor = db.rawQuery("SELECT * FROM users WHERE username=? AND password=?",
                new String[]{username, password});
        if (cursor.moveToFirst()) {
            Toast.makeText(this, "Login Successful", Toast.LENGTH_SHORT).show();
        } else {
            Toast.makeText(this, "Invalid Creditionals", Toast.LENGTH_SHORT).show();
        }
    }
    private void registerUser(){
        String username = editUsername.getText().toString();
        String password = editPassword.getText().toString();

        ContentValues values = new ContentValues();
        values.put("username", username);
        values.put("password", password);

        long result = db.insert("users", null, values);
        if (result == -1){
            Toast.makeText(this, "Registration Failed", Toast.LENGTH_SHORT).show();
        } else {
            Toast.makeText(this, "User Registered Successfully", Toast.LENGTH_SHORT).show();
        }
    }
}