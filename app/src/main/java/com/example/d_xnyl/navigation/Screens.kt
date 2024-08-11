package com.example.d_xnyl.navigation

sealed class Screens(val route: String) {
    data object LandingPage: Screens(route = "landing_page")
    data object ProfilePage: Screens(route = "profile_page")
    data object CalendarPage: Screens(route = "calendar_page")
    data object NotificationsPage: Screens(route = "notifications_page")
}