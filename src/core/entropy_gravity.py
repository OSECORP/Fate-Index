import math

def calculate_gradient(nodes, subject_pos):
    """
    nodes: list of dicts [{'x': x, 'y': y, 'z': z, 'm': mass}]
    subject_pos: dict {'x': x, 'y': y, 'z': z}
    """
    grad = {'x': 0.0, 'y': 0.0, 'z': 0.0}
    
    for node in nodes:
        dx = node['x'] - subject_pos['x']
        dy = node['y'] - subject_pos['y']
        dz = node['z'] - subject_pos['z']
        
        r = math.sqrt(dx**2 + dy**2 + dz**2)
        if r == 0: continue
        
        # Сила гравитации узла судьбы: M / r^3
        force = node['m'] / (r**3)
        
        grad['x'] += force * dx
        grad['y'] += force * dy
        grad['z'] += force * dz
        
    return grad
