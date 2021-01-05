def jogging(workout_time, speed, reduce, kkal):
    res = workout_time * 60 * speed // 1000 * kkal
    return res, res - reduce >= 0
