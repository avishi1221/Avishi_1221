using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{
    public float playerspeed; // Speed of the player
    private Rigidbody2D rb; // Rigidbody component
    private Vector2 playerDirection; // Direction of movement

    void Start()
    {
        rb = GetComponent<Rigidbody2D>(); // Get the Rigidbody2D component
    }

    void Update()
    {
        // Get vertical input (W/S or Up/Down arrows by default)
        float directionY = Input.GetAxisRaw("Vertical");
        playerDirection = new Vector2(0, directionY).normalized;
    }

    void FixedUpdate()
    {
        // Set velocity for movement
        rb.linearVelocity = new Vector2(0, playerDirection.y * playerspeed);
    }
}
