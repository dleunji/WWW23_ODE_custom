import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-dataset',
                        help='name of dataset;',
                        type=str,
                        choices=['shakespeare', 'synthetic', 'fashionmnist', 'CIFAR', 'CIFAR100-20','HAR', 'HARBOX'],
                        required=True)
    parser.add_argument('-model',
                        help='name of model;',
                        type=str,
                        required=True)
    parser.add_argument('--num-rounds',
                        help='number of rounds to simulate;',
                        type=int,
                        default=-1)
    parser.add_argument('--eval-every',
                        help='evaluate every ____ rounds;',
                        type=int,
                        default=-1)
    parser.add_argument('--clients-per-round',
                        help='number of clients trained per round;',
                        type=int,
                        default=-1)
    parser.add_argument('--seed',
                        help='random seed for reproducibility;',
                        type=int,
                        default=0)
    parser.add_argument('--batch-size',
                        help='batch size when clients train on data;',
                        type=int,
                        default=None)
    parser.add_argument('--minibatch',
                        help='None for FedAvg, else fraction;',
                        type=float,
                        default=None)
    parser.add_argument('--num-epochs',
                        help='number of epochs when clients train on data;',
                        type=int,
                        default=5)
    parser.add_argument('-t',
                        help='simulation time: small, medium, or large;',
                        type=str,
                        choices=['small', 'medium', 'large'],
                        default='large')
    parser.add_argument('-lr',
                        help='learning rate for local optimizers;',
                        type=float,
                        default=1.0,
                        required=True)
    parser.add_argument('--lr-decay',
                        help='decay in learning rate',
                        type=float,
                        default=1.0)
    parser.add_argument('--decay-lr-every',
                        help='number of iterations to decay learning rate',
                        type=int,
                        default=100)
    parser.add_argument('-reg_param',
                        help='regularization learning parameter',
                        type=float,
                        default=None)
    parser.add_argument('--aggregation',
                        help='Aggregation technique used to combine updates or gradients',
                        choices=['FedAvg'],
                        default='FedAvg')
    parser.add_argument('--gpu',
                        help='Which gpu to use. Unspecified (=None) means CPU',
                        type=int)
    parser.add_argument('--choosing-method',
                        help='method of selecting data;',
                        type=str,
                        choices=['Dream', 'Estimation', 'Coor+FIFO', 'Coor+Dream', 'Coor+Estimation1', 'Coor+Estimation2', 'Coor+Estimation2+Sim', 'Coor+FIFO', 'Estimation1', 'Estimation2', 'Estimation3'],
                        required=True
    )
    parser.add_argument('--buffer-size',
                        help='buffer size;',
                        type=int,
                        required=True
    )
    parser.add_argument('--noisy-clients-ratio',
                        help='ratio of noisy clients;',
                        type=float,
                        default=-1
    )
    parser.add_argument('--noisy-data-ratio',
                        help='ratio of noisy data;',
                        type=float,
                        default=-1
    )
    parser.add_argument('--noise-coor',
                        help='noise parameters of information matrix for coordination',
                        type=str,
                        default = '0.0-0.0'
    )
    parser.add_argument('--heterogeneity',
                        help='decide the heterogeneity level of data',
                        type=str,
                        default='data'
                        )

    args = parser.parse_args()
    
    return args