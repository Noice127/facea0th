# facea0th
Face verification system or being able to use your face as a type of authentication. 

## FaceLock
```python
import facea0th

facea0th.face_lock()
```
This takes a picture of your face, which will be your password and this is what you will need to verify your face later. 
It will also save your face in a file called "face.png"
If you want to change the file it saves in do this:
```python
import facea0th

facea0th.face_lock("YOUR_FILENAME")
```

## Face_Verify

```python
import facea0th

facea0th.face_verify("YOUR_FILENAME")
```
This will compare your face from Facelock to your face in Face_Verify.




### Code written by MadGeek (xAI Organization)
