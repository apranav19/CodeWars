from song_scheduling import SongScheduler

# Instantiate a scheduler
s = SongScheduler()

def test_case1():
	duration = [3,5,4,11]
	tone = [2,1,3,1]
	time = 17

	expected_res = 3
	actual_res = s.max_songs(duration, tone, time)

	assert expected_res == actual_res


def test_case2():
	duration = [100,200,300]
	tone = [1,2,3]
	time = 10

	expected_res = 0
	actual_res = s.max_songs(duration, tone, time)

	assert expected_res == actual_res

def test_case3():
	duration = [1,2,3,4]
	tone = [1,1,1,1]
	time = 100

	expected_res = 4
	actual_res = s.max_songs(duration, tone, time)

	assert expected_res == actual_res

def test_case4():
	duration = [10,10,10]
	tone = [58,58,58]
	time = 30

	expected_res = 3
	actual_res = s.max_songs(duration, tone, time)

	assert expected_res == actual_res

def test_case5():
	duration = [8, 11, 7, 15, 9, 16, 7, 9]
	tone = [3, 8, 5, 4, 2, 7, 4, 1]
	time = 14

	expected_res = 1
	actual_res = s.max_songs(duration, tone, time)

	assert expected_res == actual_res

def test_case6():
	duration = [5611,39996,20200,56574,81643,90131,33486,99568,48112,97168,5600,49145,73590,3979,94614]
	tone = [2916,53353,64924,86481,44803,61254,99393,5993,40781,2174,67458,74263,69710,40044,80853]
	time = 302606

	expected_res = 8
	actual_res = s.max_songs(duration, tone, time)

	assert expected_res == actual_res