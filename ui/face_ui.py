# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 11:24:55 2023

@author: USER
"""

import streamlit as st
import cv2
from face_app import detect_faces, face_cascade, cap


def main():
    
    st.tittle('Face Detection App')
    
    
    detect_faces()
    
    
if __name__ == '__main__':
    main()
    