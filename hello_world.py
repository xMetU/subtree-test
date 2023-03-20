import subtrees.hello_world as subtree
import submodules.hello_world as submodule

def main():
    subtree_test()

def subtree_test():
    subtree.hello_world()
    print(subtree.hello_world_string())

def submodule_test():
    submodule.hello_world()
    print(submodule.hello_world_string())

if __name__ == "__main__":
    main()