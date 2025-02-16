import streamlit as st
import os
from PIL import Image

st.set_page_config(page_title="NBA Shot Prediction - Visuals", layout="wide")

st.title("🏀 NBA Shot Prediction - Model Insights & Visualizations")

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
    "Feature Importance": "feature_importance.png"
}

additional_images = {
    "Confusion Matrix": "Confusion matrix.png",
    "ROC Curve": "AUC-ROC.png"
}

tab_keys = list(image_paths.keys())
tab_objects = st.tabs(tab_keys)

for tab, key in zip(tab_objects, image_paths.keys()):
    with tab:
        st.subheader(f"📊 {key} Insights")

        if os.path.exists(image_paths[key]):
            image = Image.open(image_paths[key])
            st.image(image, use_container_width=True)
        else:
            st.error("⚠️ Image file not found! Please ensure the file exists in the correct directory.")

        # Add insights
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

        elif key == "Feature Importance":
            st.write("- The most influential features are **shot distance, close defender distance, and shot difficulty**, while player attributes surprisingly played a less significant role.")
            st.write("- **The model relies heavily on defensive and distance-based metrics,** indicating that external game conditions influence shot success more than individual player attributes.")

# --- Second section: STACKED VERTICAL VISUALIZATIONS ---
st.markdown("---")
st.subheader("📊 Additional Insights & Visualizations")

for key, img_path in additional_images.items():
    st.subheader(f"📌 {key}")
    
    if os.path.exists(img_path):
        image = Image.open(img_path)
        st.image(image, use_container_width=True)
    else:
        st.error("⚠️ Image file not found! Please ensure the file exists in the correct directory.")

    if key == "Confusion Matrix":
        st.write("- The confusion matrix evaluates **how well the model classifies made and missed shots**.")
        st.write("- **Made shots (Actual - True Positive): 4195**")
        st.write("- **Missed shots (Actual - True Negative): 12532**")
        st.write("- **Incorrectly Predicted Makes (False Positives - Type 1 Error): 2145**")
        st.write("- **Incorrectly Predicted Misses (False Negatives - Type 2 Error): 8018**")
        st.write("- **Inference:** The model is **better at predicting missed shots**. Teams can leverage these insights to optimize both defensive and offensive strategies.")

    elif key == "ROC Curve":
        st.write("- The **ROC curve evaluates trade-offs between precision and recall**.")
        st.write("- **AUC scores between 0.61 and 0.65, which is reasonable** for NBA analytics and demonstrate a decent level of predictive power in shot success analysis.")

st.markdown("📌 **Scroll down for more insights!**")
