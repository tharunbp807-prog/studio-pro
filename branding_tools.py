from moviepy.editor import *

# ADD INTRO VIDEO
def add_intro(intro_path, main_video_path, output):

    # Load intro video
    intro = VideoFileClip(intro_path)

    # Load main video
    main_video = VideoFileClip(main_video_path)

    # Combine intro + main video
    final_video = concatenate_videoclips([intro, main_video])

    # Save output
    final_video.write_videofile(output)


# LOGO WATERMARK
def add_logo(video_path, logo_path, output):

    # Load video
    video = VideoFileClip(video_path)

    # Load logo image
    logo = (
        ImageClip(logo_path)
        .set_duration(video.duration)
        .resize(height=80)
        .set_position(("right", "bottom"))
        .set_opacity(0.5)
    )

    # Combine video + logo
    final = CompositeVideoClip([video, logo])

    # Save output
    final.write_videofile(output)


# TEXT WATERMARK
def add_text(video_path, text, output):

    # Load video
    video = VideoFileClip(video_path)

    # Create text
    txt = (
        TextClip(
            text,
            fontsize=40,
            color='white'
        )
        .set_duration(video.duration)
        .set_position("center")
    )

    # Combine video + text
    final = CompositeVideoClip([video, txt])

    # Save output
    final.write_videofile(output)


# EXAMPLE USAGE

add_intro(
    "intro.mp4",
    "main_video.mp4",
    "final_output.mp4"
)
