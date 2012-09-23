package boostingPig.datasets;

import java.io.IOException;
import java.util.Random;

import org.apache.hadoop.mapreduce.InputFormat;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.RecordReader;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.pig.LoadFunc;
import org.apache.pig.backend.executionengine.ExecException;
import org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.PigSplit;
import org.apache.pig.data.DataByteArray;
import org.apache.pig.data.Tuple;
import org.apache.pig.data.TupleFactory;

import weka.core.Instance;
import weka.core.Instances;
import weka.core.Utils;
import weka.datagenerators.DataGenerator;
import weka.datagenerators.classifiers.classification.RDG1;

public class DataGeneratorLoadFunc extends LoadFunc{

	private RecordReader reader;
	private final TupleFactory tupleFactory = TupleFactory.getInstance();

	private DataGenerator dataGen;
	private Instances insts;
	private int count = 0;
	private int max = 0;	
	
	public DataGeneratorLoadFunc() throws Exception {
		this("weka.datagenerators.classifiers.classification.RDG1 -r weka.datagenerators.classifiers.classification.RDG1-S_1_-n_100_-a_100_-c_2_-N_100_-I_0_-M_1_-R_10 -S 1 -n 100 -a 100 -c 2 -N 100 -I 0 -M 1 -R 10");
	}
	
	public DataGeneratorLoadFunc(String arg) throws Exception {
		this.dataGen = new RDG1();
		this.dataGen.setOptions(Utils.splitOptions(arg));
	}	
	
	@Override
	public InputFormat getInputFormat() throws IOException {
		return new TextInputFormat();
	}
	
	@Override
	public void setLocation(String location, Job job) throws IOException {
		FileInputFormat.setInputPaths(job, location);
	}	
	
	@Override
	public void prepareToRead(RecordReader reader, PigSplit split)
			throws IOException {
		this.reader = reader;
	}	

	@Override
	public Tuple getNext() throws IOException {
		try {
			if (reader.nextKeyValue()) {
				reader.getCurrentValue();

				Tuple tuple = tupleFactory.newTuple();
				
				checkInstances();
				String inst = insts.instance(count++).toString();
				tuple.append(new DataByteArray(inst));

				return tuple;
			}
			return null;
		} catch (InterruptedException e) {
			throw new ExecException(e);
		}
	}
	
	private void checkInstances() {
		if (count >= max) {
			try {
				insts = ((RDG1)dataGen).generateExamples(1000, new Random(), dataGen.defineDataFormat());
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
