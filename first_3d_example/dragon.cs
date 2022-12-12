using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using UnityEngine.SceneManagement;

public class dragon : MonoBehaviour{

    private Transform transform;
    public float speed;
    public float flightSpeed;
    private Animator animator;

    void Start(){
        transform = GetComponent<Transform>();
        animator = GetComponent<Animator>();
    }//end start()

    void Update(){
        float currentX = transform.position.x;
        float currentY = transform.position.y;
        float currentZ = transform.position.z;

        float forward = Input.GetAxis("Vertical");
        float sideways = Input.GetAxis("Horizontal");

        if(forward != 0 || sideways != 0){
            animator.SetBool("walking", true);
            Vector3 newPosition = new Vector3(currentX + sideways*speed, currentY, currentZ + forward*speed);
            transform.position = newPosition;
        }
        else{
            animator.SetBool("walking", false);
        }


        float flight = Input.GetAxis("Jump");
        if(flight != 0 ){
            animator.SetBool("flying", true);
            if(currentY < 20){
                Vector3 flightPosition = new Vector3(currentX, currentY + flight*flightSpeed, currentZ);
                transform.position = flightPosition;
            }
        }
        else{
            animator.SetBool("flying", false);
        }
    }//end update()



    void OnCollisionEnter(Collision collision){
        if(collision.gameObject.tag == "gateway"){
            if(SceneManager.GetActiveScene().name == "desert"){
               SceneManager.LoadScene("meadow"); 
            }
            else if(SceneManager.GetActiveScene().name == "meadow"){
                SceneManager.LoadScene("desert");
            }
        }
        else if(collision.gameObject.tag == "enemy"){
            SceneManager.LoadScene(SceneManager.GetActiveScene().name);
        }
        else if(collision.gameObject.tag == "npc"){
            Debug.Log("Why hello there...");
        }
    }
}//end dragon class
