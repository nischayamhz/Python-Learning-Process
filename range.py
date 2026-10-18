#Write a program that calculates kinetic energy for a mass of 1000 kg at velocities 20,40,60,80,100m/s
mass=1000
for velocity in range(20,101,20):
    KE=0.5*mass*velocity**2
    print("Velocity:", velocity,"m/s| Kinetic Energy:", KE,"J")