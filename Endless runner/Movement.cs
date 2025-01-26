using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Movement : MonoBehaviour
{
    private Transform Player;

    private bool Lane1 = false;
    private bool Lane2 = true;
    private bool Lane3 = false;

    private bool up = false;

    public Material[] mat_sky;

    private void Start()
    {
        Player = GetComponent<Transform>();
        RenderSettings.skybox=mat_sky[Random.Range(0 , 5)];//create random skybox 1-5
    }

    private void Update()
    {
        if(Lane3 == true && Player.position.z < 1.1f)
        {
            Player.position += new Vector3(0, 0, 10.5f * Time.deltaTime);
        }
        else if(Lane1 == true && Player.position.z > -1.1f)
        {
            Player.position += new Vector3(0, 0, -10.5f * Time.deltaTime);
        }
        else if(Lane2 == true && Player.position.z <= -0.1f)
        {
            Player.position += new Vector3(0, 0, 10.5f * Time.deltaTime);
        }
        else if(Lane2 == true && Player.position.z >= 0.1f)
        {
            Player.position += new Vector3(0, 0, -10.5f * Time.deltaTime);
        }



        #region ChangeBools
        if (SwipeManager.swipeRight == true && Lane3 == false && Lane1 == true)
        {
            Lane2 = true;
            Lane1 = false;
            Lane3 = false;
        }
        else if (SwipeManager.swipeLeft == true && Lane2 == true && Player.position.z <= 0.2f)
        {
            Lane1 = true;
            Lane2 = false;
            Lane3 = false;
        }
        else if (SwipeManager.swipeRight == true && Lane2 == true && Player.position.z >= -0.2f)
        {
            Lane3 = true;
            Lane1 = false;
            Lane2 = false;
        }
        else if (SwipeManager.swipeLeft == true && Lane1 == false && Lane3 == true)
        {
            Lane2 = true;
            Lane1 = false;
            Lane3 = false;
        }
        #endregion

       
       
        if (SwipeManager.swipeUp == true && Player.position.y <= 0f && up ==false)
        {
            up = true;
           
        }

        if(up == true && Player.position.y <= 1.6f)
        {
            Player.position += new Vector3(0, +5.0f * Time.deltaTime , 0);
        }
        else if(Player.position.y > 0f)
        {
           up = false;
           Player.position += new Vector3(0, -5.0f * Time.deltaTime , 0);  
        }
        else if(Player.position.y < 0f)
        {
           Player.position += new Vector3(0, 0 , 0);  
        }


        RenderSettings.skybox.SetFloat("_Rotation", Time.time * 5.0f); //rotate skybox

        
        
    }
}
