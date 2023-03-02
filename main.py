from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    stop_music=int(input("Press 2 to stop music anytime:  "))
    if stop_music==2:
      source.paused = True
      return
    else:
      continue

while True:
  os.system("clear")
  print("My Out of This World Playlist 🎶🎵🎸🎧")
  time.sleep(5)
  print("Press 1 to continue")
  time.sleep(2)
  print("Press 2 to exit")
  user=int(input())
  if user == 1:
    print("Let's Jam!!! 🎸")
    play()
  elif user == 2:
    exit()
  else:
    continue
