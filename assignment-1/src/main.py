import argparse
import graph

def init_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("-d", type=str, required=True)
  parser.add_argument("--alg", type=str, required=True)

  return parser

def main():
  args = init_args().parse_args()

  graphs = graph.read_all(args.d)


if __name__ == "__main__":
  main()