import streamlit as st
import os
from PIL import Image

st.set_page_config(page_title="NBA Shot Prediction - Visuals", layout="wide")

st.title("🏀 NBA Shot Prediction - Model Insights & Visualizations")

st.markdown(
            "⬅️ ** Click on the first tab and then Swipe left/right or use left/right arrow keys to better explore the tabs** ➡️"
        )

image_paths = {
    "Height vs Shot Distance": "Height vs Shot distance.png",
    "Weight vs Shot Distance": "Weight vs Shot distance.png",
    "Position vs Shot Distance": "Position vs Shot disance.png",
    "Simpson's Paradox - Overall": "Simpsons Paradox for overall.png",
    "Simpson's Paradox - Position C": "Simpsons Paradox for Position C.png",
    "Simpson's Paradox - Position PG": "Simpsons Paradox for Position PG.png",
    "Evolution of Shot Types": "Evolution of Shot types.png",
    "Feature Correlation Heatmap": "Correlation Heatmap.png",
    "Model Comparison - Test Accuracy": "Model Accuracy.png",
    "Confusion Matrix": "Confusion matrix.png",
    "ROC Curve": "AUC-ROC.png",
    "Feature Importance": "feature_importance.png"
}

tabs = list(image_paths.keys())
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12 = st.tabs(tabs)

for tab, key in zip([tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12], image_paths.keys()):
    with tab:
        st.subheader(f"📊 {key} Insights")

        if os.path.exists(image_paths[key]):
            image = Image.open(image_paths[key])
            st.image(image, use_container_width=300)
        else:
            st.error("⚠️ Image file not found! Please ensure the file exists in the correct directory.")

        if key == "Height vs Shot Distance":
            st.write("- **Taller players tend to take shots closer to the basket** as they have a natural advantage near the rim.")
            st.write("- **There is a slight positive correlation** between height and shot distance, indicating that taller players have an **efficiency edge near the basket**.")

        elif key == "Weight vs Shot Distance":
            st.write("- **Heavier players generally take shorter shots**, likely due to their dominant presence on the court.")
            st.write("- **Guards and lighter players tend to take shots from farther away from the basket.** Our analysis also reveals that taller players are naturally heavier.")
            st.write("- **Weight does not strongly influence FG%**, highlighting that **skill and positioning matter more** than physique in basketball.")

        elif key == "Position vs Shot Distance":
            st.write("- **Player position significantly influences shot selection** and effectiveness.")
            st.write("- **Guards typically take longer shots**, including more three-pointers, while centers take the shortest ones by leveraging their **proximity to the basket**.")
            st.write("- **Centers and power forwards have higher FG%** due to taking more high-percentage shots near the hoop. Guards contribute more to long-range scoring.")

        elif key == "Simpson's Paradox - Overall":
            st.write("- **Simpson’s Paradox** highlights how overall trends can be misleading when data is not segmented properly.")
            st.write("- **At the overall level, heavier and taller players tend to have higher FG%.**")
            st.write("- However, when analyzed by position, this relationship **does not necessarily hold**. Centers—who are the tallest and heaviest—already take high-percentage shots, so within their position, weight and height **do not strongly impact FG% further**.")
            st.write("- **Similarly, for point guards, taller players do not always have higher FG%.** This is because PGs take more difficult shots, and their shooting efficiency depends more on shot selection rather than height alone.")
            st.write("- **This paradox highlights the importance of breaking down data by player roles rather than relying only on overall trends.**")

        elif key == "Simpson's Paradox - Position C":
            st.write("- **At the overall level, heavier players appear to have a positive correlation with FG%,** but within their own position, this trend does not necessarily continue.")
            st.write("- **Centers already take high-percentage shots near the rim,** so among centers alone, weight/height differences **do not have a significant impact on FG%**.")
            st.write("- **This paradox occurs because positional roles dictate shot selection.** While centers are naturally the heaviest players and have high FG%, their efficiency is **driven more by shot type than just weight alone.**")

        elif key == "Simpson's Paradox - Position PG":
            st.write("- **Point guards, at an overall level, appear to have a lower FG% compared to other positions.**")
            st.write("- However, when analyzed by position, **taller point guards do not always have a significant FG% advantage over shorter ones**.")
            st.write("- **This is because PGs take more difficult shots—long-range threes, pull-ups, and contested jumpers—which reduces their overall shooting efficiency.**")
            st.write("- **This highlights why breaking down data by position is essential.** FG% is not just about height/weight, but about **the type of shots a player is taking.**")

        elif key == "Evolution of Shot Types":
            st.write("- The **NBA has evolved into a perimeter-oriented game**, with a sharp increase in **three-point attempts over the years**.")
            st.write("- By 2024, **nearly 40% of all shot attempts are from beyond the arc, compared to nearly 0% in 1980**.")

        elif key == "Feature Correlation Heatmap":
            st.write("- The heatmap highlights correlations between different features, showing which factors have the biggest impact on shot success.")

        elif key == "Model Comparison - Test Accuracy":
            st.write("- **Gradient Boosting was chosen as the final model (~62.2%)**, while Random Forest had a larger train accuracy and test accuracy gap.")
            st.write("- **Gradient Boosting performs better due to its strong generalization, lower overfitting, and better handling of complex relationships in NBA shot prediction.**")

        elif key == "ROC Curve":
            st.write("- The **ROC curve evaluates trade-offs between precision and recall**.")
            st.write("- **AUC scores between 0.61 and 0.65, which is reasonable** for NBA analytics and demonstrate a decent level of predictive power in shot success analysis.")

        elif key == "Feature Importance":
            st.write("- The most influential features are **shot distance, close defender distance, and shot difficulty**, while player attributes surprisingly played a less significant role.")
            st.write("- **The model relies heavily on defensive and distance-based metrics,** indicating that external game conditions influence shot success more than individual player attributes.")

        elif key == "Confusion Matrix":
            st.write("- The confusion matrix evaluates **how well the model classifies made and missed shots**.")
            st.write("- **Made shots (Actual - True Positive): 4195**")
            st.write("- **Missed shots (Actual - True Negative): 12532**")
            st.write("- **Incorrectly Predicted Makes (False Positives - Type 1 Error): 2145**")
            st.write("- **Incorrectly Predicted Misses (False Negatives - Type 2 Error): 8018**")
            st.write("- **Inference:** The model is **better at predicting missed shots**. Teams can leverage these insights to optimize both defensive and offensive strategies.")
