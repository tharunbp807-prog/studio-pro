from moviepy import (
    VideoFileClip,
    ImageClip,
    TextClip,
    CompositeVideoClip,
    concatenate_videoclips
)

# ADD INTRO VIDEO
def add_intro(intro_path, main_video_path, output):

    intro = VideoFileClip(intro_path)
    main_video = VideoFileClip(main_video_path)

    final_video = concatenate_videoclips(
        [intro, main_video]
    )

    final_video.write_videofile(output)


# LOGO WATERMARK
def add_logo(video_path, logo_path, output):

    video = VideoFileClip(video_path)

    logo = (
        ImageClip(logo_path)
        .with_duration(video.duration)
        .resized(height=80)
        .with_position(("right", "bottom"))
    )

    final = CompositeVideoClip([video, logo])

    final.write_videofile(output)


# TEXT WATERMARK
def add_text(video_path, text, output):

    video = VideoFileClip(video_path)

    txt = (
        TextClip(
            text=text,
            font_size=40,
            color="white"
        )
        .with_duration(video.duration)
        .with_position("center")
    )

    final = CompositeVideoClip([video, txt])

    final.write_videofile(output)
