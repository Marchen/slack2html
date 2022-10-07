import argparse

from converter import SlackToHTMLConverter

# %%
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("in_dir")
    parser.add_argument("out_dir")
    args = parser.parse_args()

    SlackToHTMLConverter(args.in_dir).convert(args.out_dir)
