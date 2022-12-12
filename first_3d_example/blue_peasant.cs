using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class blue_peasant : MonoBehaviour
{
     
    private Transform transform;
    public float speed;
    private int direction;
    private int frame;


    void Start(){
        transform = GetComponent<Transform>();
        direction = Random.Range(1, 8);
    }

    void Update(){
        float currentX = transform.position.x;
        float currentY = transform.position.y;
        float currentZ = transform.position.z;

        

        if(frame % 550 != 0){
            if(direction == 1){
                Vector3 newPosition = new Vector3(currentX, currentY, currentZ + speed);
                transform.position = newPosition;
            }
            else if(direction == 2){
                Vector3 newPosition = new Vector3(currentX + speed/Mathf.Sqrt(2), currentY, currentZ + speed/Mathf.Sqrt(2));
                transform.position = newPosition;
            }
            else if(direction == 3){
                Vector3 newPosition = new Vector3(currentX + speed, currentY, currentZ);
                transform.position = newPosition;
            }
            else if(direction == 4){
                Vector3 newPosition = new Vector3(currentX - speed/Mathf.Sqrt(2), currentY, currentZ + speed/Mathf.Sqrt(2));
                transform.position = newPosition;
            }
            else if(direction == 5){
                Vector3 newPosition = new Vector3(currentX, currentY, currentZ - speed);
                transform.position = newPosition;
            }
            else if(direction == 6){
                Vector3 newPosition = new Vector3(currentX - speed/Mathf.Sqrt(2), currentY, currentZ - speed/Mathf.Sqrt(2));
                transform.position = newPosition;
            }
            else if(direction == 7){
                Vector3 newPosition = new Vector3(currentX - speed, currentY, currentZ);
                transform.position = newPosition;
            }
            else{
                Vector3 newPosition = new Vector3(currentX + speed/Mathf.Sqrt(2), currentY, currentZ - speed/Mathf.Sqrt(2));
                transform.position = newPosition;
            }
            // Vector3 newPosition = new Vector3(currentX, currentY, currentZ + speed);
            // transform.position = newPosition;
        }
        else{
            direction = Random.Range(1, 8);
        }

        frame++;
    }//end update()
}
