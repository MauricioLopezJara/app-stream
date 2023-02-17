import os

import streamlit as st

# These are the formats supported in Streamlit right now.
VIDEO_EXTENSIONS = ["mp4", "ogv", "m4v", "webm"]

# For sample video files, try the Internet Archive, or download a few samples here:
# http://techslides.com/sample-webm-ogg-and-mp4-video-files-for-html5


st.title("Video Widget Examples")

st.header("Local video files")
st.write(
    "You can use st.video to play a locally-stored video by supplying it with a valid filesystem path."
)


def get_video_files_in_dir(directory):
    out = []
    for item in os.listdir(directory):
        try:
            name, ext = item.split(".")
        except:
            continue
        if name and ext:
            if ext in VIDEO_EXTENSIONS:
                out.append(item)
    return out


avdir = os.path.expanduser("~")
files = get_video_files_in_dir(avdir)

if len(files) == 0:
    st.write(
        "Put some video files in your home directory (%s) to activate this player."
        % avdir
    )

else:
    filename = st.selectbox(
        "Select a video file from your home directory (%s) to play" % avdir,
        files,
        0,
    )

    st.video(os.path.join(avdir, filename))
st.header("Remote video playback")
st.write("st.video allows a variety of HTML5 supported video links, including YouTube.")


def shorten_vid_option(opt):
    return opt.split("/")[-1]


# A random sampling of videos found around the web.  We should replace
# these with those sourced from the streamlit community if possible!
vidurl = st.selectbox(
    "Pick a video to play",
    (
        "https://www.youtube.com/watch?v=GKevHTbVsbQ&list=RDGKevHTbVsbQ&start_radio=1",
        "https://www.youtube.com/watch?v=NxhzI18PnH8",
        "https://www.youtube.com/watch?v=mg-T-EhXLoE"
    ),
    0,
    shorten_vid_option,
)

st.video(vidurl)