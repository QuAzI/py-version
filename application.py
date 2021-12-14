import version


def main():
    print(f"Version: {version.__version__}")
    print(version.generate_rc())


if __name__ == '__main__':
    main()
