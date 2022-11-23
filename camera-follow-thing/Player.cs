using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour{
    

    private Transform transform;
    public float speed;

    public void Start(){
        transform = GetComponent<Transform>();
    }

    public void Update(){

        float hor = Input.GetAxis("Horizontal");
        float ver = Input.GetAxis("Vertical");

        if(hor != 0 && transform.position.x > -41 && transform.position.x < 41){
            Vector2 pos = new Vector2(transform.position.x + hor*speed, transform.position.y);
            transform.position = pos;
        }

        if(ver != 0 && transform.position.y > -5.7 && transform.position.y < 5.7){
            Vector2 pos = new Vector2(transform.position.x, transform.position.y + ver*speed);
            transform.position = pos;
        }


        
    }
}
