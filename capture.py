# This project is to capture the web cam footage

# Imprting the modules
import cv2


# Create an object for the camera. Zero for the external camera
videoCamera = cv2.VideoCapture(0)

# Initializing the frame count
frameCount = 0

while True:

    # Increasing the timer by one
    frameCount = frameCount + 1

    # Create a frame object
    check, frame = videoCamera.read()

    # Showing the matrix
    print(frame)

    # Display the frame
    cv2.imshow("Capturing",frame)


    # Wait for a key being pressed
    key = cv2.waitKey(1)

    # If the key is q then stop the loop
    if key == ord("q"):
        break

# Print to total number of frames
print(frameCount)

# Shutdown the camera
videoCamera.release()

# Destroy all the windows
cv2.destroyAllWindows()
