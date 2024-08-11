package com.example.d_xnyl

import com.google.firebase.messaging.FirebaseMessagingService
import com.google.firebase.messaging.RemoteMessage

class PushNotificationService:FirebaseMessagingService() {

    override fun onNewToken(token: String) { //to record new refresh tokens
        super.onNewToken(token)
    }
    override fun onMessageReceived(message: RemoteMessage) {
        //to perform actions on receiving msg, customise the msgs
        super.onMessageReceived(message)
    }

}