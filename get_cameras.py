import cv2
import os

max_cameras = 4
output_dir = "test_images"
os.makedirs(output_dir, exist_ok=True)

try:
    # Loop through camera indices to test each available camera
    for camera_index in range(max_cameras):
        cap = cv2.VideoCapture(camera_index)
        if cap.isOpened():
            print(f"Successfully accessed camera with index {camera_index}")
            ret, frame = cap.read()
            if ret:
                # Save the frame as an image in the test_images folder
                file_path = os.path.join(output_dir, f"captured_image_{camera_index}.png")
                counter = 1
                while os.path.exists(file_path):
                    file_path = os.path.join(output_dir, f"captured_image_{camera_index}_{counter}.png")
                    counter += 1

                cv2.imwrite(file_path, frame)
                print(f"Image saved at {file_path}")
            else:
                print(f"Failed to grab frame from camera with index {camera_index}")
            cap.release()  # Release the resource after testing the camera
        else:
            print(f"Camera with index {camera_index} is not available")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    cv2.destroyAllWindows()
    print("All cameras have been tested and windows have been closed.")