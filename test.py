# # import streamlit as st
# # from streamlit_webrtc import webrtc_streamer

# # st.set_page_config(page_title="WebRTC Test")

# # st.title("🎥 WebRTC Camera Test")

# # webrtc_streamer(
# #     key="test",
# #     media_stream_constraints={
# #         "video": True,
# #         "audio": False,
# #     }
# # )
# import streamlit as st
# from streamlit_webrtc import webrtc_streamer, WebRtcMode

# st.title("WebRTC Test")

# ctx = webrtc_streamer(
#     key="test",
#     mode=WebRtcMode.SENDRECV,
#     rtc_configuration={
#         "iceServers": [
#             {"urls": ["stun:stun.l.google.com:19302"]}
#         ]
#     },
#     media_stream_constraints={
#         "video": True,
#         "audio": False,
#     },
# )

# st.write(ctx.state)
import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.title("WebRTC Test")

webrtc_streamer(
    key="test",
    media_stream_constraints={
        "video": True,
        "audio": False,
    },
)