Skinsense - Personalized Skincare Recommendation System
Project Overview
Skinsense is a comprehensive skincare recommendation system that combines a machine learning model with a robust backend API to provide personalized skincare advice.

Backend API Endpoints
1. User Management

User Registration: /User/userRegister
User Login: /Login/userLogin
Get User Details: /User/getUserByUsername
Update User Profile: /User/updateUser
Change Password: /User/changePassword

2. Ingredient Management

Insert Ingredients: /Ingredient/InsertIngredients
Get All Ingredients: /Ingredient/getAllIngredient
Get Ingredient by Name: /Ingredient/getIngredByName

3. Alarm System

Insert Alarm: /Alarm/insertAlarm
Get Alarms by Username: /Alarm/getAlarmByUsername
Get Alarms by Date: /Alarm/getAlarmByDate

4. Scan History

Insert Scan History: /History/insertHistory
Get Scan History by Username: /History/getHistoryByUsername
Get Scan History by Date: /History/getHistoryByUsernameDate

API Base URL
https://dynamic-reef-344016.uc.r.appspot.com
Authentication
Most endpoints require Bearer Token authentication obtained from /Login/userLogin
