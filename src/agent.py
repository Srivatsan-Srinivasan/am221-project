import tensorflow as tf

flags = tf.app.flags
FLAGS = flags.FLAGS

flags.DEFINE_integer('warmup', 2000, 'time without training but only filling the replay memory')
flags.DEFINE_integer('bsize', 256, 'minibatch size')
flags.DEFINE_integer('iter', 1, 'train iters each timestep')
flags.DEFINE_integer('l1size', 200, '1st layer size')
flags.DEFINE_integer('l2size', 200, '2nd layer size')
flags.DEFINE_integer('rmsize', 100000, 'memory size')

flags.DEFINE_float('tau', 0.01, 'moving average for target network')
flags.DEFINE_float('discount', 0.99, 'gamma')
flags.DEFINE_float('l2norm', 0.0001, 'l2 weight decay')
flags.DEFINE_float('pl2norm', 0.001, 'policy network l2 weight decay (only for DDPG)')
flags.DEFINE_float('rate', 0.001, 'learning rate')
flags.DEFINE_float('prate', 0.0001, 'policy net learning rate (only for DDPG)')
flags.DEFINE_float('outheta', 0.15, 'noise theta') # large theta -> small noise
flags.DEFINE_float('ousigma', 0.2, 'noise sigma') # minimum noise
flags.DEFINE_float('lrelu', 0.01, 'leak relu rate')


flags.DEFINE_boolean('use_per', True, 'enable Prioritized Experience Replay')
flags.DEFINE_float('alpha', 0.6, 'prioritized experience replay')
flags.DEFINE_float('beta0', 0.9, 'prioritized experience replay')
flags.DEFINE_float('beta_iters', 100000, 'prioritized experience replay')
flags.DEFINE_float('eps', 1e-6, 'prioritized experience replay')

flags.DEFINE_boolean('naf_bn', False, 'enable NAF batch normalization')
flags.DEFINE_boolean('icnn_bn', False, 'enable icnn batch normalization')


flags.DEFINE_string('icnn_opt', 'adam',
                    "ICNN's inner optimization routine. Options=[adam,bundle_entropy]")

flags.DEFINE_integer('thread', 1, 'tensorflow threads')

flags.DEFINE_boolean('adam_plot', False, 'show adam plot')
flags.DEFINE_boolean('summary', False, 'use tensorboard log')

flags.DEFINE_float('initstd', 0.01, 'weight init std (DDPG uses its own initialization)')
