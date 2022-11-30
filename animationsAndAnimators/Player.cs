using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour{
    
    private Transform transform;
    public GameObject image;
    public float speed;
    public float jumpSpeed;
    public Animator animator;
    public LayerMask groundLayer;
    

    void Start(){
        transform = GetComponent<Transform>();
    }

    void Update(){
        float hor = Input.GetAxis("Horizontal");
        float jump = Input.GetAxis("Jump");
        float currentX = transform.position.x;
        float currentY = transform.position.y;
        float xMovement = currentX + hor*speed;
        float jumpMovement = currentY + jumpSpeed;
        if(jump > 0){
            Vector2 jumpPosition = new Vector2(currentX, jumpMovement);
            transform.position = jumpPosition;
            animator.SetBool("attacking", true);
        }
        else if(hor > 0){
            Vector2 newPosition = new Vector2(xMovement, currentY);
            transform.position = newPosition;
            image.transform.localScale = new Vector2(6.0f, 6.0f);
        }
        else if(hor < 0){
            Vector2 newPosition = new Vector2(xMovement, currentY);
            transform.position = newPosition;
            image.transform.localScale = new Vector2(-6.0f, 6.0f);
        }


        Vector2 origin = transform.position;
        Vector2 direction = Vector2.down;

        float distanceThreshold = 2;
        

        RaycastHit2D hit = Physics2D.Raycast(origin, direction, distanceThreshold, groundLayer);

        if(hit && animator.GetBool("attacking")){
            animator.SetBool("attacking", false);
            Debug.Log("on the ground");
        }

    }
}
