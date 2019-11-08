test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest

. ssshtest

STRUCTURE='binary'
FILE='sorted.txt'
SIZE=10000
run binary_tree_add python insert_key_value_pairs.py \
	--data_structure $STRUCTURE \
	--data_size $SIZE \
	--dataset $FILE
assert_exit_code 0

run nonexisting_data_structure python insert_key_value_pairs.py \
        --data_structure 'foo' \
        --data_size $SIZE \
        --dataset $FILE
assert_exit_code 1

run nonexisting_file python insert_key_value_pairs.py \
        --data_structure $STRUCTURE \
        --data_size $SIZE \
        --dataset 'foo'
assert_exit_code 1

run bad_size python insert_key_value_pairs.py \
        --data_structure $STRUCTURE \
        --data_size 11000 \
        --dataset $FILE
assert_exit_code 1

STRUCTURE='hash'
run test_hash python insert_key_value_pairs.py \
	--data_structure $STRUCTURE \
	--data_size 100 \
	--dataset $FILE
assert_in_stdout "hash"
assert_exit_code 0

STRUCTURE='binary'
run test_binary python insert_key_value_pairs.py \
        --data_structure $STRUCTURE \
        --data_size 100 \
        --dataset $FILE
assert_in_stdout "binary"
assert_exit_code 0

STRUCTURE='avl'
run test_avl python insert_key_value_pairs.py \
        --data_structure $STRUCTURE \
        --data_size 100 \
        --dataset $FILE
assert_in_stdout "avl"
assert_exit_code 0
