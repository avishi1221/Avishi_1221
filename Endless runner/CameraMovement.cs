using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraMovement : MonoBehaviour
{ 
     public float cameraspeed; // Speed of the camera
    

    void Update()
    {
        transform.position+= new Vector3(cameraspeed  *Time.deltaTime,0,0);
    }
}
   

