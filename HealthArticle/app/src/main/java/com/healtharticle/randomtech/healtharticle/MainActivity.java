package com.healtharticle.randomtech.healtharticle;

import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void monkeys(View v) {
        Uri uri = Uri.parse("https://edition.cnn.com/2018/02/02/health/fda-monkey-deaths-animal-studies-explainer/index.html"); // missing 'http://' will cause crashed
        Intent intent = new Intent(Intent.ACTION_VIEW, uri);
        startActivity(intent);
    }
    public void ancient(View v) {
        Uri uri = Uri.parse("https://edition.cnn.com/2018/02/02/health/india-stones-history-ad-trnd/index.html"); // missing 'http://' will cause crashed
        Intent intent = new Intent(Intent.ACTION_VIEW, uri);
        startActivity(intent);
    }
    public void emt(View v) {
        Uri uri = Uri.parse("https://edition.cnn.com/2018/02/02/health/iyw-new-emt-meets-lifesaver-trnd/index.html"); // missing 'http://' will cause crashed
        Intent intent = new Intent(Intent.ACTION_VIEW, uri);
        startActivity(intent);
    }
    public void cancer(View v) {
        Uri uri = Uri.parse("https://edition.cnn.com/2018/02/02/health/prostate-cancer-breast-cancer-uk-intl/index.html"); // missing 'http://' will cause crashed
        Intent intent = new Intent(Intent.ACTION_VIEW, uri);
        startActivity(intent);
    }
    public void rare(View v) {
        Uri uri = Uri.parse("https://edition.cnn.com/2018/02/02/health/viking-graves-repton/index.html"); // missing 'http://' will cause crashed
        Intent intent = new Intent(Intent.ACTION_VIEW, uri);
        startActivity(intent);
    }
    public void baby(View v) {
        Uri uri = Uri.parse("https://edition.cnn.com/2018/02/02/health/lactalis-baby-milk-powder-salmonella-intl/index.html"); // missing 'http://' will cause crashed
        Intent intent = new Intent(Intent.ACTION_VIEW, uri);
        startActivity(intent);
    }
}
