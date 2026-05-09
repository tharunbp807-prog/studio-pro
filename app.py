import streamlit as st
from branding_tools import *

# PAGE SETTINGS
st.set_page_config(
    page_title="Creator Studio Pro",
    layout="wide"
)

# TITLE
st.title("🎬 Creator Studio Pro")

# SIDEBAR MENU
menu = st.sidebar.selectbox(
    "Choose Feature",
    [
        "Logo Watermark",
        "Text Watermark"
    ]
)

# INTRO VIDEO UPLOAD
intro_video = st.file_uploader(
    "Upload Intro Video",
    type=["mp4"]
)

# MAIN VIDEO UPLOAD
video = st.file_uploader(
    "Upload Main Video",
    type=["mp4"]
)

# CHECK VIDEO
if video:

    # SAVE MAIN VIDEO
    with open("temp/input.mp4", "wb") as f:
        f.write(video.read())

    st.success("Main Video Uploaded Successfully")

    # SAVE INTRO VIDEO
    if intro_video:

        with open("temp/intro.mp4", "wb") as f:
            f.write(intro_video.read())

        st.success("Intro Video Uploaded Successfully")

        # COMBINE INTRO + MAIN VIDEO
        add_intro(
            "temp/intro.mp4",
            "temp/input.mp4",
            "temp/combined.mp4"
        )

        final_input = "temp/combined.mp4"

    else:
        final_input = "temp/input.mp4"

    # LOGO WATERMARK
    if menu == "Logo Watermark":

        logo = st.file_uploader(
            "Upload Logo",
            type=["png"]
        )

        if logo:

            # SAVE LOGO
            with open("temp/logo.png", "wb") as f:
                f.write(logo.read())

            # BUTTON
            if st.button("Add Logo Watermark"):

                add_logo(
                    final_input,
                    "temp/logo.png",
                    "outputs/logo_output.mp4"
                )

                st.success("Logo Added Successfully!")

                # SHOW VIDEO
                st.video("outputs/logo_output.mp4")
