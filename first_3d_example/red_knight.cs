using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class red_knight : MonoBehaviour {
    
    private Transform transform;
    public float speed;
    public GameObject dragon;
    private int frame;
    public float distanceThreshold;


    void Start(){
        transform = GetComponent<Transform>();
    }

    void Update(){
        float currentX = transform.position.x;
        float currentY = transform.position.y;
        float currentZ = transform.position.z;

        float playerX = dragon.transform.position.x;
        float playerY = dragon.transform.position.y;
        float playerZ = dragon.transform.position.z;

        float distanceToPlayer = Mathf.Sqrt( (playerX - currentX)*(playerX - currentX) + (playerZ - currentZ)*(playerZ - currentZ));
        if(distanceToPlayer < distanceThreshold){
            float moveX = (playerX - currentX) / distanceToPlayer;
            float moveZ = (playerZ - currentZ) / distanceToPlayer;
            Vector3 movement = new Vector3(currentX + moveX*speed, currentY, currentZ + moveZ*speed);
            transform.position = movement;

        }
        else if(frame % 470 < 190){
            Vector3 newPosition = new Vector3(currentX, currentY, currentZ + speed);
            transform.position = newPosition;
        }
        else if(frame % 470 < 190+65){
            Vector3 newPosition = new Vector3(currentX + speed, currentY, currentZ);
            transform.position = newPosition;
        }
        else if(frame % 470 < 190+65+190){
            Vector3 newPosition = new Vector3(currentX, currentY, currentZ - speed);
            transform.position = newPosition;
        }
        else if(frame % 470 < 190+65+190+64){
            Vector3 newPosition = new Vector3(currentX - speed, currentY, currentZ);
            transform.position = newPosition;
        }

        frame++;
    }//end update()
}
