echo "data_structure,data_size,data_file,add_time,search_time,nonexistant_search_time" > benchmarking.txt
for i in {1000..10000..1000}
do
FILE=rand.txt
STRUCTURE='hash'
python insert_key_value_pairs.py \
        --data_structure $STRUCTURE \
        --data_size $i \
        --dataset $FILE >> benchmarking.txt

STRUCTURE='avl'
python insert_key_value_pairs.py \
        --data_structure $STRUCTURE \
        --data_size $i \
        --dataset $FILE >> benchmarking.txt

STRUCTURE='binary'
python insert_key_value_pairs.py \
        --data_structure $STRUCTURE \
        --data_size $i \
        --dataset $FILE >> benchmarking.txt

FILE=sorted.txt
STRUCTURE='hash'
python insert_key_value_pairs.py \
        --data_structure $STRUCTURE \
        --data_size $i \
        --dataset $FILE >> benchmarking.txt

STRUCTURE='avl'
python insert_key_value_pairs.py \
        --data_structure $STRUCTURE \
        --data_size $i \
        --dataset $FILE >> benchmarking.txt

STRUCTURE='binary'
python insert_key_value_pairs.py \
        --data_structure $STRUCTURE \
        --data_size $i \
        --dataset $FILE >> benchmarking.txt
done
