package com.example.d_xnyl.navigation

import android.app.Notification
import androidx.compose.runtime.Composable
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.example.d_xnyl.MainViewModel
import com.example.d_xnyl.screens.CalendarPage
import com.example.d_xnyl.screens.LandingPage
import com.example.d_xnyl.screens.NotificationsPage
import com.example.d_xnyl.screens.ProfilePage

@Composable
fun Navigation() {
    val navController = rememberNavController()
    val viewModel:MainViewModel = viewModel<MainViewModel>()

    NavHost(
        navController = navController,
        startDestination = Screens.LandingPage.route,

        ) {
        composable(route = Screens.LandingPage.route) {
            LandingPage(navController = navController)
        }
        composable(route = Screens.ProfilePage.route) {
            ProfilePage(navController = navController)
        }
        composable(route = Screens.CalendarPage.route) {
            CalendarPage(navController = navController)
        }
        composable(route = Screens.NotificationsPage.route) {
            NotificationsPage(navController = navController)
        }
    }
}