using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour{

    Rigidbody2D body;

    void Start(){

        body = GetComponent<Rigidbody2D>();
        
    }//end start()




    void Update(){

        float hor = Input.GetAxis("Horizontal");
        float ver = Input.GetAxis("Jump");
        if(ver > 0.5){
            body.velocity = new Vector2(body.velocity.x, 7.5f);
        }

        if(hor > 0){
            body.velocity = new Vector2(1.2f, body.velocity.y);
        }
        else if(hor < 0){
            body.velocity = new Vector2(-1.2f, body.velocity.y);
        }

        
    }//end Update()



}//end class
