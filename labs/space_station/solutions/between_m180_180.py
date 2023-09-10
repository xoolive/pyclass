def between_m180_180(angle):
    return np.degrees(np.angle(np.exp(1j*np.radians(angle))))

between_m180_180(-350)
