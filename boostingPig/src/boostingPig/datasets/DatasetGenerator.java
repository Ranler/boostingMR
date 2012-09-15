package boostingPig.datasets;

import java.io.IOException;
import java.util.Random;

import org.apache.pig.EvalFunc;
import org.apache.pig.data.Tuple;

import weka.core.Instance;
import weka.core.Instances;
import weka.core.Utils;
import weka.datagenerators.DataGenerator;
import weka.datagenerators.classifiers.classification.RDG1;

public class DatasetGenerator extends EvalFunc<String>{
	
	private DataGenerator dataGen;
	private Instances insts;
	private int count = 0;
	private int max = 0;

	public DatasetGenerator(String arg) throws Exception {
		//String arg = "weka.datagenerators.classifiers.classification.RDG1 -r weka.datagenerators.classifiers.classification.RDG1-S_1_-n_100_-a_100_-c_2_-N_100_-I_0_-M_1_-R_10 -S 1 -n 100 -a 100 -c 2 -N 100 -I 0 -M 1 -R 10";		
		dataGen = new RDG1();
		dataGen.setOptions(Utils.splitOptions(arg));
	}
	
	@Override
	public String exec(Tuple t) throws IOException {
		checkInstances();
		return insts.instance(count++).toString();
	}
	
	private void checkInstances() {
		if (count >= max) {
			try {
				insts = ((RDG1)dataGen).generateExamples(100, new Random(), dataGen.defineDataFormat());
			} catch (Exception e) {
				e.printStackTrace();
			}
			max = insts.numInstances();
			count = 0;
		}
	}
	
	public static void main(String[] args) throws Exception {
		String arg = "weka.datagenerators.classifiers.classification.RDG1 -r weka.datagenerators.classifiers.classification.RDG1-S_1_-n_100_-a_100_-c_2_-N_100_-I_0_-M_1_-R_10 -S 1 -n 100 -a 100 -c 2 -N 100 -I 0 -M 1 -R 10";		
		RDG1 rdg1 = new RDG1();
		String[] options = Utils.splitOptions(arg);
		rdg1.setOptions(options);
		Instances insts = rdg1.generateExamples(100, new Random(), rdg1.defineDataFormat());
		for (Instance inst : insts) {
			System.out.println(inst.toString());
		}
	}

}