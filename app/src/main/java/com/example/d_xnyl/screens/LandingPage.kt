package com.example.d_xnyl.screens

import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Rect
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.RectangleShape
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController
import androidx.navigation.compose.rememberNavController
import com.example.d_xnyl.ui.theme.DeltaColorBright
import com.example.d_xnyl.ui.theme.DeltaColorDark

@Composable
fun LandingPage(navController: NavController) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(color = Color.Black),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.SpaceEvenly
    ) {
        Text(
            text = "{D_XNYL}",
            fontWeight = FontWeight.W900,
            color = Color.White,
            fontSize = 75.sp
        )

        OutlinedButton(
            onClick = {
                navController.navigate("profile_page")
            },
            shape = RectangleShape,
            colors = ButtonDefaults.buttonColors(
                containerColor = DeltaColorDark
            ),
            border = BorderStroke(width = 1.dp, color = DeltaColorBright)
        ) {
            Text(text = "Login with DAuth")
        }
    }
}

@Preview
@Composable
private fun LandingPreview() {
    LandingPage(navController = rememberNavController())
}